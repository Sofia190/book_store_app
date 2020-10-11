from django.contrib import admin

# Register your models here.


from .models import AccountSettings, ContactInformation, MailMessage



admin.site.register(AccountSettings)
admin.site.register(ContactInformation)
admin.site.register(MailMessage)


























