from django.urls import path
from . import views

urlpatterns = [
    path("add_available_flight_details/", views.add_available_flight_details),
    path("get_available_flights/", views.get_available_flights),
    path("get_available_flights_for_passion_air/", views.get_available_flights_for_passion_air),
    path("get_available_flights_for_awa/", views.get_available_flights_for_awa),
    path("book_flight/<int:flight_id>/", views.book_flight),
    path("get_all_my_booked_flights/", views.get_all_my_booked_flights),
    path("get_all_booked_flights/", views.get_all_booked_flights),
    path("delete_flight/<int:id>/",views.delete_flight),

#     request flight
    path("request_flight/<int:flight_id>/",views.request_flight),
    path("get_all_my_requested_flights/",views.get_all_my_requested_flights),
    path("get_all_requested_flights/",views.get_all_requested_flights),
    path("delete_flight/<int:id>/",views.delete_flight),

#     search flight
    path("search_flight/<str:depart_date>/<str:airline>/",views.search_flight)
]