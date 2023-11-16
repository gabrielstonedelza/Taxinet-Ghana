from django.urls import path
from . import views

urlpatterns = [
    path("request_flight/", views.request_flight),
    path("get_my_flight_requests/", views.get_my_flight_requests),
    path("get_all_flight_requests/", views.get_all_flight_requests),
    path("delete_flight/<int:id>/",views.delete_flight),
    path("add_to_booked/<int:id>/",views.add_to_booked),
    path("get_my_booked_flights/",views.get_my_booked_flights),
    path("get_booked_flights/",views.get_booked_flights),
]