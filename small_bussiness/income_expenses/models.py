from django.db import models

# Create your models here.
class Income(models.Model):

    def __str__(self):
        return str(self.date) + ' : ' + str(self.income_sum) + ' €'
    
    income_cash = models.FloatField()
    income_pos = models.FloatField()
    income_sum = models.FloatField()
    date = models.DateField()
