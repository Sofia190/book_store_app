
from django.conf import settings

from django.db import models

# Create your models here.

from django.utils import timezone

from datetime import timedelta, datetime, date


from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL  


from django.db.models import Q







class TranslatorQuerySet(models.query.QuerySet):

	
	def Translator_name_items(self, value):
		return self.filter(name__icontains='name')


	def search(self, query):
		lookup = (
				 Q(name__icontains=query) |
				 Q(location__icontains=query) |
				 Q(subject_1__icontains=query) |
				 Q(subject_2__icontains=query) |
				 Q(subject_3__icontains=query) |
				 Q(work_1__icontains=query) |
				 Q(work_2__icontains=query) |
				 Q(work_3__icontains=query) |
				 Q(work_4__icontains=query) |
				 Q(work_5__icontains=query) |
				 Q(work_6__icontains=query) |
				 Q(work_7__icontains=query) |
				 Q(work_8__icontains=query) |
				 Q(work_9__icontains=query) |
				 Q(work_10__icontains=query) |
				 Q(work_11__icontains=query) |
				 Q(work_12__icontains=query) )




		return self.filter(lookup)





class TranslatorModelManager(models.Manager):


	def get_queryset(self):
		    return TranslatorQuerySet(self.model, using=self._db)



	def search(self, query=None):
			if query is None:
				return self.get_queryset.none()
			return self.get_queryset().search(query)

	



	def get_time_frame(self, date1, date2):
    		qs=self.get_queryset()
    		qs_time_1 = qs.filter(birth_date__gte=date1)
    		qs_time_2=qs_time_1.filter(birth_date__lt=date2) 

    		return qs_time_2




		   

	def get_time_frame_20th(self):

		qs_20th=self.get_queryset().order_by('name')

		l_20 = []

		for item in qs_20th:

			if (item.birth_date > date(1900,12,31) 
				and item.birth_date < date(2001,1,1)):

				l_20.append(item)

		return l_20

				


	



	def get_time_frame_21st(self):

		qs_21th=self.get_queryset().order_by('name')


		l_21 = []

		for item in qs_21th:

			if (item.birth_date > date(1999,12,31)
				and item.birth_date < date(2101, 1, 1)):

				l_21.append(item)

		return l_21




	def retrieve_sorted_subjects_20(self):

		qs_20th=self.get_queryset()


		l_20 = []

		for item in qs_20th:

			if (item.birth_date > date(1900,12,31) 
				and item.birth_date < date(2001,1,1)):

				l_20.append(item)



		l_subjects_sorted = []

		for item in l_20:

			l_subjects_sorted.append(item.subject_1)
			l_subjects_sorted.append(item.subject_2)
			l_subjects_sorted.append(item.subject_3)

			l_subjects_sorted.sort()

		return l_subjects_sorted






	def retrieve_sorted_subjects_21(self):

		qs_21th=self.get_queryset()


		l_21 = []

		for item in qs_21th:

			if (item.birth_date > date(1999,12,31) 
				and item.birth_date < date(2101,1,1)):

				l_21.append(item)



		l_subjects_sorted = []

		for item in l_21:

			l_subjects_sorted.append(item.subject_1)
			l_subjects_sorted.append(item.subject_2)
			l_subjects_sorted.append(item.subject_3)

			l_subjects_sorted.sort()

		return l_subjects_sorted




	def retrieve_sorted_works_20(self):

		qs_20th=self.get_queryset()


		l_20 = []

		for item in qs_20th:

			if (item.birth_date > date(1900,12,31) 
				and item.birth_date < date(2001,1,1)):

				l_20.append(item)



		l_works_sorted = []

		for item in l_20:

			l_works_sorted.append(item.work_1)
			l_works_sorted.append(item.work_2)
			l_works_sorted.append(item.work_3)
			l_works_sorted.append(item.work_4)
			l_works_sorted.append(item.work_5)
			l_works_sorted.append(item.work_6)
			l_works_sorted.append(item.work_7)
			l_works_sorted.append(item.work_8)
			l_works_sorted.append(item.work_9)
			l_works_sorted.append(item.work_10)
			l_works_sorted.append(item.work_11)
			l_works_sorted.append(item.work_12)

			l_works_sorted.sort()

		return l_works_sorted



	def retrieve_sorted_works_21(self):

		qs_20th=self.get_queryset()


		l_20 = []

		for item in qs_20th:

			if (item.birth_date > date(1999,12,31) 
				and item.birth_date < date(2101,1,1)):

				l_20.append(item)



		l_works_sorted = []

		for item in l_20:

			l_works_sorted.append(item.work_1)
			l_works_sorted.append(item.work_2)
			l_works_sorted.append(item.work_3)
			l_works_sorted.append(item.work_4)
			l_works_sorted.append(item.work_5)
			l_works_sorted.append(item.work_6)
			l_works_sorted.append(item.work_7)
			l_works_sorted.append(item.work_8)
			l_works_sorted.append(item.work_9)
			l_works_sorted.append(item.work_10)
			l_works_sorted.append(item.work_11)
			l_works_sorted.append(item.work_12)

			l_works_sorted.sort()

		return l_works_sorted





	def retrieve_sorted_works(self, id):

		obj = self.get_queryset().get(id=id)

		l_works_sorted = []

		l_works_sorted.append(obj.work_1)
		l_works_sorted.append(obj.work_2)
		l_works_sorted.append(obj.work_3)
		l_works_sorted.append(obj.work_4)
		l_works_sorted.append(obj.work_4)
		l_works_sorted.append(obj.work_5)
		l_works_sorted.append(obj.work_6)
		l_works_sorted.append(obj.work_7)
		l_works_sorted.append(obj.work_8)
		l_works_sorted.append(obj.work_9)
		l_works_sorted.append(obj.work_10)
		l_works_sorted.append(obj.work_11)

		l_works_sorted.sort()

		return l_works_sorted




	def display_sorted_authors(self):

		qs=self.get_queryset().order_by('name')

		return qs




	def display_sorted_subjects(self):


		qs = self.get_queryset()

		l_subjects_sorted = []

		for obj in qs:

			l_subjects_sorted.append(obj.subject_1)
			l_subjects_sorted.append(obj.subject_2)
			l_subjects_sorted.append(obj.subject_3)
			

			l_subjects_sorted.sort()

		return l_subjects_sorted




	




class Translator(models.Model):

	name = models.CharField(max_length=50, default='translator')
	location = models.CharField(max_length=70, default='place of birth')
	birth_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())
	subject_1 = models.CharField(max_length=100, default='first subject')
	subject_2 = models.CharField(max_length=100, default='second subject')
	subject_3 = models.CharField(max_length=100, default='third subject')



	work_1 = models.CharField(max_length=200, default='first work')
	work_1_description = models.TextField(default='first work description')

	work_2 = models.CharField(max_length=200, default='second work')
	work_2_description = models.TextField(default='second work description')

	work_3 = models.CharField(max_length=200, default='third work')
	work_3_description = models.TextField(default='third work description')

	work_4 = models.CharField(max_length=200, default='fourth work', null=True)
	work_4_description = models.TextField(default='fourth work description')

	work_5 = models.CharField(max_length=200, default='fifth work', null=True)
	work_5_description = models.TextField(default='fifth work description')

	work_6 = models.CharField(max_length=200, default='sixth work', null=True)
	work_6_description = models.TextField(default='sixth work description')

	work_7 = models.CharField(max_length=200, default='seventh work', null=True)
	work_7_description = models.TextField(default='seventh work description')

	work_8 = models.CharField(max_length=200, default='eight work', null=True)
	work_8_description = models.TextField(default='eight work description')

	work_9 = models.CharField(max_length=200, default='nineth work', null=True)
	work_9_description = models.TextField(default='nineth work description')

	work_10 = models.CharField(max_length=200, default='tenth work', null=True)
	work_10_description = models.TextField(default='10th work description')

	work_11 = models.CharField(max_length=200, default='eleventh work', null=True)
	work_11_description = models.TextField(default='eleventh work description')

	work_12 = models.CharField(max_length=200, default='twelveth work', null=True)
	work_12_description = models.TextField(default='twelveth work description')



	item_1 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_2 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_3 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_4 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_5 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_6 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_7 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_8 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_9 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_10 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_11 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_12 = models.FileField(upload_to='image/', blank=True, null=True, default=None)


	item_13 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_14 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_15 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_16 = models.FileField(upload_to='image/', blank=True, null=True, default=None)

	item_17 = models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	item_18 = models.FileField(upload_to='image/', blank=True, null=True, default=None)





	card_1= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_2= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_3= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_4= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_5= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_6= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_7= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_8= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_9= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_10= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_11= models.ImageField(upload_to='image/', blank=True, null=True, default=None)

	card_12= models.ImageField(upload_to='image/', blank=True, null=True, default=None)


	objects = TranslatorModelManager() 


	def __str__(self):
		return self.name






class Work(models.Model):

	translator = models.ForeignKey(Translator, on_delete=models.CASCADE, default=True)
	name = models.CharField(max_length=200, default='name')
	description = models.TextField(default='description')


	 


	





















