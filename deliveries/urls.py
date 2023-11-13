from django.urls import path
from . import views

urlpatterns = [
    path("request_delivery/",views.request_delivery),
    path("get_my_delivery_requests/",views.get_my_delivery_requests),
    path("get_all_deliveries/",views.get_all_deliveries),
    path("delete_delivery/<int:id>/",views.delete_delivery),
]