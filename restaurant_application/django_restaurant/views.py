from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Ingredients, MenuItem, Purchase
from .forms import IngredientsForm, MenuItemForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def home(request):
    return render(request, 'django_restaurant\index.html')

# ----------------- List Views
class IngredientsList(LoginRequiredMixin,ListView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_list.html'
    ingredient_list = Ingredients.objects.all()

class MenuItemList(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_list.html'


class PurchaseList(LoginRequiredMixin,ListView):
    model = Purchase
    template_name ='django_restaurant\purchase_list.html'


class ProfitAndRevenueView(LoginRequiredMixin,ListView):
    model = Purchase
    template_name ='django_restaurant\profit_and_revenue_list.html'

# ----------------- Create Views
class IngredientsCreate(LoginRequiredMixin,CreateView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_create.html'
    form_class = IngredientsForm

class MenuItemCreate(LoginRequiredMixin,CreateView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_create.html'
    form_class = MenuItemForm


# ----------------- Update Views

class IngredientsUpdate(LoginRequiredMixin,UpdateView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_update.html'
    fields = '__all__'

class MenuItemUpdate(LoginRequiredMixin,UpdateView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_update.html'
    fields = '__all__'

# ----------------- Delete Views

class IngredientsDelete(LoginRequiredMixin,DeleteView):
    model = Ingredients
    template_name = 'django_restaurant\ingredients_delete.html'
    
    def get_success_url(self):
        return '/ingredients_list/'

    
class MenuItemDelete(LoginRequiredMixin,DeleteView):
    model = MenuItem
    template_name = 'django_restaurant\menu_item_delete.html'

    def get_success_url(self):
        return '/menu_item_list/'

# ----------------- Registration Views

def login_page(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "registration/login.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("home")


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"