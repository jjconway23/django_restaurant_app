from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredients, MenuItem, Purchase
from .forms import IngredientsForm, MenuItemForm
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

class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_create.html'
    form_class = MenuItemForm


# ----------------- Create Views

class IngredientsUpdate(UpdateView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_update.html'
    fields = '__all__'

class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_update.html'
    fields = '__all__'

# ----------------- Create Views

class IngredientsDelete(DeleteView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_delete.html'
    
    def get_success_url(self):
        return '/ingredients_list/'