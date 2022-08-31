from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Ingredients, MenuItem, Purchase
def home(request):
    return render(request, 'django_restaurant\index.html')


class IngredientsList(ListView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_list.html'

class MenuItemList(ListView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_list.html'


class PurchaseList(ListView):
    model = Purchase
    template_name ='django_restaurant\purchase_list.html'