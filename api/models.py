from django.db import models

# A simple model which includes name location and ssnumber
# ____________________________
# |_____name_____|__string___|
# |___location___|__string___|
# |___ssnumber___|__Integer__|
#

class Socialsecurity(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    ssnumber = models.IntegerField()