from django.db import models

# Create your models here.
class Income(models.Model):
    income_cash = models.FloatField()
    income_pos = models.FloatField()
    income_sum = models.FloatField()
    date = models.DateField()
    