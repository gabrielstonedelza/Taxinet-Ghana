from django.urls import path

from . import views

urlpatterns = [
    path("add_vehicle/",views.add_vehicle),
    path("add_vehicle_image/",views.add_vehicle_image),
    path("get_all_vehicles_images/<int:id>/",views.get_all_vehicles_images),
    path("delete_purchase/<int:id>/",views.delete_purchase),
    path("delete_vehicle/<int:id>/",views.delete_vehicle),
    path("get_all_vehicles/",views.get_all_vehicles),
    path("get_my_purchase_requests/",views.get_my_purchase_requests),
    path("get_all_purchase_requests/",views.get_all_purchase_requests),
]