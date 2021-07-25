from django.db import models
from django.db.models.fields import FloatField, IntegerField

# Create your models here.
class YearlyGDP(models.Model):
    year = IntegerField(max_length=4 , null=False)
    gdp_growth = FloatField(null=False)

    def __str__(self):
         return str(self.year)