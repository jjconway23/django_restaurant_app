from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2)


