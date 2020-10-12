
from django.conf import settings



from django.db import models

# Create your models here.

from django.utils import timezone


from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL   #auth.User


from Translator.models import Translator






class Item_to_buy_work(models.Model):

	name = models.CharField(max_length=270)
	price = models.IntegerField(default=0)
	available = models.BooleanField(default=True)
	ships_to_America = models.BooleanField(default=True)
	ships_to_Romania = models.BooleanField(default=True)
	shipping_period = models.IntegerField(default=0)
	translator = models.ManyToManyField(Translator, blank=True)



	
	
class Item_to_buy_card(models.Model):

	name = models.CharField(max_length=270)
	price = models.IntegerField(default=0)
	available = models.BooleanField(default=True)
	ships_to_America = models.BooleanField(default=True)
	ships_to_Romania = models.BooleanField(default=True)
	shipping_period = models.IntegerField(default=0)
	translator = models.ManyToManyField(Translator, blank=True)







class OrdersQuerySet(models.query.QuerySet):


	def Order_name_items(self, value):
		return self.filter(total_price__gt=20)





class OrdersModelManager(models.Manager):


	def get_queryset(self):
		    return OrdersQuerySet(self.model, using=self._db)




	# def calculate_total_price(self, request, id):

	# 		qs = self.get_queryset().filter(user=request.user).get(id=id)


	# 		for i in qs.works.all():

	# 			qs.total_price += i.price  

	# 		for k in qs.cards.all():

	# 			qs.total_price += k.price

	# 		var = qs.total_price

	# 		return var


	
	
	def calculate_total_price(self, request):

			qs = self.get_queryset().filter(user=request.user)

			l_price = []

			for i in qs:

				for j in i.works.all():

					i.total_price += j.price  


				for k in i.cards.all():

					i.total_price += k.price

				l_price.append(i.total_price)


			var = l_price

			return var




	# def display_items_count(self, request, id):

	# 		count = 0

	# 		qs = self.get_queryset().filter(user=request.user).get(id=id)

	# 		for item in qs.works.all():

	# 			count += 1

	# 		for item in qs.cards.all():

	# 			count += 1

	# 		return count

		




	def calculate_total_price_works(self, request):

			qs = self.get_queryset().filter(user=request.user).filter(returned=False)

			var = 0

			for i in qs:

				for j in i.works.all():

					print(j.price)

					var+=j.price

			return var



		
	def calculate_total_price_works_detail(self, request, id):

			qs = self.get_queryset().filter(user=request.user).get(id=id)

			var = 0

			for i in qs.works.all():

				print(i.price)

				var+=i.price

			return var





	def calculate_total_price_cards(self, request):

			qs = self.get_queryset().filter(user=request.user).filter(returned=False)

			var = 0

			for i in qs:

				for j in i.cards.all():

					print(j.price)

					var+=j.price

			return var




	def calculate_total_price_cards_detail(self, request, id):

			qs = self.get_queryset().filter(user=request.user).get(id=id)

			var = 0

			for i in qs.cards.all():

				print(i.price)

				var+=i.price

			return var




	def set_orders_total_price(self, request):


			qs = self.get_queryset().filter(user=request.user).filter(returned=False)

			var = 0
			var1 = 0

			for i in qs:

				for j in i.works.all():

					print(j.price)

					var+=j.price

				for k in i.cards.all():

					print(k.price)

					var1+=k.price


			return var+var1



	def set_orders_total_price_detail(self, request, id):


			qs = self.get_queryset().filter(user=request.user).get(id=id)

			var = 0
			var1 = 0

			for i in qs.works.all():

				print(i.price)

				var+=i.price

			for k in qs.cards.all():

				print(k.price)

				var1+=k.price


			return var+var1



	def retrieve_orders_not_returned(self, request):

		qs = Orders.objects.filter(user=request.user).filter(returned=False)

		return qs


	def retrieve_items_sorted_by_quantities(self, request):

		return Orders.objects.filter(user=request.user).order_by('items_count')




	def retrieve_items_sorted_by_total_price(self, request):

		return Orders.objects.filter(user=request.user).order_by('-items_value')



	def retrieve_items_sorted_by_date_field(self, request):

		return Orders.objects.filter(user=request.user).order_by('-date_field')



	def retrieve_orders_associated(self, request):

    		return Orders.objects.filter(user=request.user)



   
  


class Orders(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
	date_field = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	from_person = models.CharField(max_length=350)
	from_person_address = models.TextField(default="Al. Compozitorilor Nr.6A, Bucharest, Romania")
	total_price = models.IntegerField(default=0)
	items_value = models.IntegerField(default=0)
	validity_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	works = models.ManyToManyField(Item_to_buy_work)
	cards = models.ManyToManyField(Item_to_buy_card)
	translator = models.ManyToManyField(Translator, blank=True)
	returned = models.BooleanField(default=False)
	items_count = models.IntegerField(default=0)


	def retrieve_items_price(self):

		
		for item in self.works.all():
			self.total_price+=item.price

		for item in self.cards.all():
			self.total_price+=item.price

		return self.total_price



	# def retrieve_items_count(self):


	# 	for item in self.works.all():
	# 		self.items_count += 1

	# 	for item in self.cards.all():
	# 		self.items_count +=1

	# 	return self.items_count

		

	objects = OrdersModelManager()




	#def cancel_after_end_date(request):

		#if (self.validity_date + timedelta(days=1) == timezone.now()):

			#self.delete()






class Bills(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)  
	orders = models.ManyToManyField(Orders)
	company_name = models.CharField(max_length=200)
	active  = models.BooleanField(default=True)
	date_field = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	total_price = models.IntegerField(default=0)




class Returned_items(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)  
	orders = models.ManyToManyField(Orders)
	count = models.IntegerField(default=0)
	return_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
   





