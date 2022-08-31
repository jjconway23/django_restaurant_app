from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50, blank=False)
    quantity = models.IntegerField(blank=False)
    unit = models.CharField(max_length=20, blank=False)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2, blank=False)


class MenuItem(models.Model):
    title = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
