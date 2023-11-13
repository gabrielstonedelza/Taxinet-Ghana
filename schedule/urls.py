from django.urls import path
from . import views

urlpatterns = [
    path("request_ride/",views.request_ride),
    path("get_all_my_schedules/",views.get_all_my_schedules),
    path("get_all_schedules/",views.get_all_schedules),
    path("delete_schedule/<int:id>/",views.delete_schedule),
]