from django.db import models

# Create your models here.
class Socialsecurity(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    ssnumber = models.IntegerField()