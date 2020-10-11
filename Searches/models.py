from django.db import models

# Create your models here.

from django.conf import settings

from django.db import models

from django.utils import timezone





# Create your models here.

class SearchQuery(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
	query = models.CharField(max_length=570)
	timestamp = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now())












	
	
	
	
