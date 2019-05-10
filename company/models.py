from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Company(models.Model):
    name = models.Charfield(max_length=250)
    estd = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    description = models.Textfield()
    vat_number = models.CharField(max_length=40, blank=False, null=False)
    address = models.CharField(max_length=300)