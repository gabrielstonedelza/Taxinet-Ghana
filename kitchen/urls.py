from django.urls import path
from . import views

urlpatterns = [
    path("menu_preview/",views.menu,name="menu_preview"),
    path("food_menu/",views.food_menu,name="food_menu"),
    path("add_food_item/",views.add_food_item,name="add_food_item"),
    path('menu/<int:pk>/update/', views.update_menu, name='update_menu'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
]