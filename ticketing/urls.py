from django.urls import path
from . import views

urlpatterns = [
    path("book_flight/",views.book_flight),
    path("get_my_flights/",views.get_my_flights),
    path("get_all_flights/",views.get_all_flights),
    path("delete_flight/<int:id>/",views.delete_flight),
]