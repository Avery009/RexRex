from django.db import models

# Create your models here.
class Contact(models.Model):
	contact_id = models.BigAutoField(primary_key=True,unique=True)
	contact_number = models.CharField(max_length=20, blank=False, null=False)
	contact_email = models.CharField(max_length=100, blank = False, null = False)
	contact_date = models.DateTimeField(null=False)
	contact_inquiry = models.CharField(max_length=1000,null=False)