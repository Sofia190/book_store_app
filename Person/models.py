from django.conf import settings

from django.db import models

# Create your models here.

from django.contrib.auth import get_user_model


User = settings.AUTH_USER_MODEL   #auth.User

from django.utils import timezone





class AccountSettings(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

	receive_marketing_emails = models.BooleanField(default=False)

	sort_orders_by_dates = models.BooleanField(default=True)

	sort_orders_by_quantities = models.BooleanField(default=False)

	display_most_expensive_items_at_the_top = models.BooleanField(default=False)

	display_the_most_recent_items_at_the_top = models.BooleanField(default=True)



class ContactInformation(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)
	address = models.TextField(default='your billing address')
	phone_number = models.CharField(max_length=35, default='your phone number')
	email_address = models.CharField(max_length=200, default='your email address ')






class MailMessage(models.Model):

     
    title = models.CharField(max_length=150, default='message')
    message =  models.TextField(default='Write your message here')
    from_user = models.CharField(max_length=70, default='salvetei book store')
    to_user = models.ManyToManyField(User, default=True)
    sent = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())




    





























