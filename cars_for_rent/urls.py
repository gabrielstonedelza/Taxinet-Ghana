from django.urls import path

from . import views

urlpatterns = [
    path("add_new_car_for_rent/", views.add_new_car_for_rent),
    path("all_cars_for_pay_and_drive/", views.all_cars_for_pay_and_drive),
    path("vehicle/<int:id>/", views.get_car_for_rent),
    path("get_all_vehicles_for_rent_images/<int:id>/", views.get_all_vehicles_for_rent_images),
]