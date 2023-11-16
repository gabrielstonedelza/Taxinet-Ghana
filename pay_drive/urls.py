from django.urls import path

from . import views

urlpatterns = [
    path("request_pay_and_drive/<int:id>/",views.request_pay_and_drive),
    path("get_my_pay_and_drive_requests/",views.get_my_pay_and_drive_requests),
    path("get_all_pay_and_drive_requests/",views.get_all_pay_and_drive_requests),
    path("delete_pay_and_drive/<int:id>/",views.delete_pay_and_drive),
    path("add_to_pay_and_drive_complete/<int:id>/",views.add_to_pay_and_drive_complete),
    path("get_all_my_approved_pay_and_drive/",views.get_all_my_approved_pay_and_drive),
    path("get_all_approved_pay_and_drive/",views.get_all_approved_pay_and_drive),
]