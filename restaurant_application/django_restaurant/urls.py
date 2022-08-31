from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('ingredients_list/', views.IngredientsList.as_view(), name='ingredients_list')
]