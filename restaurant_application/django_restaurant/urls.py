from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('ingredients_list/', views.IngredientsList.as_view(), name='ingredients_list'),
    path('menu_item_list/', views.MenuItemList.as_view(), name='menu_item_list'),
    path('purchase_list/', views.PurchaseList.as_view(),name='purchase_list'),
    path('profit_and_revenue_list/', views.ProfitAndRevenueView.as_view(), name='profit_and_revenue_list'),
]