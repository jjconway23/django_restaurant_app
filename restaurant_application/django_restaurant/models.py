from django.db import models

class Ingredients(models.Model):
    name = models.CharField(max_length=50, blank=False)
    quantity = models.IntegerField(blank=False)
    unit = models.CharField(max_length=20, blank=False)
    price_per_unit = models.DecimalField(max_digits=6, decimal_places=2, blank=False)


class MenuItem(models.Model):
    title = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50, blank=False)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)