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
    path('ingredients_list/delete/<pk>', views.IngredientsDelete.as_view(), name='ingredients_delete'),
    path('menu_item_list/delete/<pk>/', views.MenuItemDelete.as_view(), name='menu_item_delete'),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_view, name='logout'),
    path('signup/',views.SignUp.as_view(), name='signup'),
]