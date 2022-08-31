from ast import Mod
from django.forms import ModelForm
from .models import Ingredients, Purchase, RecipeRequirement, MenuItem

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'

class MenuItemForm(ModelForm):
    class Meta:
        model= MenuItem
        fields = '__all__'

