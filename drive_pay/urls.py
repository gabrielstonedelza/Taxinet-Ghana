from django.urls import path
from . import views

urlpatterns = [
    path("request_drive_and_pay/",views.request_drive_and_pay),
    path("get_my_drive_and_pay_requests/",views.get_my_drive_and_pay_requests),
    path("get_all_drive_and_pay_requests/",views.get_all_drive_and_pay_requests),
    path("delete_drive_and_pay/<int:id>/",views.delete_drive_and_pay),
]