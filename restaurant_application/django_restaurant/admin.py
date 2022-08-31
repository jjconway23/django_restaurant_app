from django.contrib import admin

from restaurant_application.django_restaurant.models import Ingredients, MenuItem, RecipeRequirement, Purchase

# Register your models here.
admin.site.register(Ingredients)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)
admin.site.register(Purchase)