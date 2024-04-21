# models.py in ihrer Django-App

from django.db import models

class EnergyUsage(models.Model):
    customer_number = models.CharField(max_length=3)
    year = models.CharField(max_length=10)
    highest_kw = models.FloatField()
    second_highest_kw = models.FloatField()
    usage_hours_highest_kw = models.FloatField()
    usage_hours_second_highest_kw = models.FloatField()
    year_description = models.CharField(max_length=200, default="Nicht spezifiziert")


