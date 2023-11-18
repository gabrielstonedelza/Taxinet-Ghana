from django.urls import path

from . import views

urlpatterns =[
    path("add_inventory/",views.add_inventory),
    path("get_my_inventories/",views.get_my_inventories),
    path("get_all_inventories/",views.get_all_inventories),
]