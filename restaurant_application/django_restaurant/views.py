from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredients, MenuItem, Purchase
from .forms import IngredientsForm
def home(request):
    return render(request, 'django_restaurant\index.html')

# ----------------- List Views
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

# ----------------- Create Views
class IngredientsCreate(CreateView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_create.html'
    form_class = IngredientsForm