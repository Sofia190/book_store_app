
from django.forms import ModelForm

from .models import AccountSettings, ContactInformation, MailMessage




class SettingsForm(ModelForm):

	class Meta: 

		model = AccountSettings

		fields = ['receive_marketing_emails', 'sort_orders_by_dates', 

		'sort_orders_by_quantities', 'display_most_expensive_items_at_the_top',

		'display_the_most_recent_items_at_the_top',


		]





class Add_contact_details_Form(ModelForm):

	class Meta:

		model = ContactInformation

		fields = ['address', 'phone_number', 'email_address']






class ContactInformation_Form(ModelForm):

	class Meta:

		model = ContactInformation

		fields = ['address', 'phone_number', 'email_address']




class SendMessageForm(ModelForm):

	class Meta:

		model  = MailMessage

		fields = ['from_user', 'to_user', 'title', 'message', 'sent']




























