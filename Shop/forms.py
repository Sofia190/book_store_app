from django.forms import ModelForm




from .models import Orders



class OrdersForm(ModelForm):

	class Meta: 

		model = Orders

		fields = ['works', 'cards' , 'translator']
		
































