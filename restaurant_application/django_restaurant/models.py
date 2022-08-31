from django.db import models
from django.urls import reverse

class Ingredients(models.Model):
    name = models.CharField(max_length=50, blank=False)
    quantity = models.FloatField(default=0, blank=False)
    unit = models.CharField(max_length=20, blank=False)
    price_per_unit = models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=False)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ingredients_list')

class MenuItem(models.Model):
    title = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('menu_item_list')

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.menu_item


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.menu_item} sold on {self.timestamp}"