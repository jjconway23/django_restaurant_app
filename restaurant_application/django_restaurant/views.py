from http.client import HTTPResponse
from typing import List
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Ingredients, MenuItem, Purchase
def home(request):
    return render(request, 'django_restaurant\index.html')


class IngredientsList(ListView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_list.html'
    ingredient_list = Ingredients.objects.all()

class MenuItemList(ListView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_list.html'


class PurchaseList(ListView):
    model = Purchase
    template_name ='django_restaurant\purchase_list.html'


class ProfitAndRevenueView(ListView):
    model = Purchase
    template_name ='django_restaurant\profit_and_revenue_list.html'