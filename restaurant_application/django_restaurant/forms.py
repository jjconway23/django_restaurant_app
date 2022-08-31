from django.forms import ModelForm
from .models import Ingredients, Purchase, RecipeRequirement, MenuItem

class IngredientsForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'

class MenuItem(ModelForm):
    class Meta:
        model= MenuItem
        fields = '__all__'