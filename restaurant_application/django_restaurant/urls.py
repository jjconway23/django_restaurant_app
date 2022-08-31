from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('ingredients_list/', views.IngredientsList.as_view(), name='ingredients_list'),
    path('menu_item_list/', views.MenuItemList.as_view(), name='menu_item_list'),
    path('purchase_list/', views.PurchaseList.as_view(),name='purchase_list'),
    path('profit_and_revenue_list/', views.ProfitAndRevenueView.as_view(), name='profit_and_revenue_list'),
    path('ingredients_list/create/', views.IngredientsCreate.as_view(), name='ingredients_create'),
    path('menu_item_list/create/', views.MenuItemCreate.as_view(), name='menu_item_create'),
    path('ingredients_list/update/<pk>/', views.IngredientsUpdate.as_view(), name='ingredients_update'),
    path('menu_item_list/update/<pk>/', views.MenuItemUpdate.as_view(), name='menu_item_update'),
]