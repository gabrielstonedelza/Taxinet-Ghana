from django.urls import path

from . import views

urlpatterns = [
    path("request_pay_and_drive/<int:id>/",views.request_pay_and_drive),
    path("get_my_pay_and_drive_requests/",views.get_my_pay_and_drive_requests),
    path("get_all_pay_and_drive_requests/",views.get_all_pay_and_drive_requests),
    path("delete_pay_and_drive/<int:id>/",views.delete_pay_and_drive),
    path("update_approve_pay_drive/<int:pk>/",views.update_approve_pay_drive),
    path("approve_pay_drive_request/<int:pk>/",views.approve_pay_drive_request),
    path("add_to_pay_and_drive_complete/<int:id>/",views.add_to_pay_and_drive_complete),
    path("get_all_my_approved_pay_and_drive/",views.get_all_my_approved_pay_and_drive),
    path("get_all_approved_pay_and_drive/",views.get_all_approved_pay_and_drive),
    path("add_to_pay_and_drive_extra/",views.add_to_pay_and_drive_extra),
    path("get_all_my_extra_payment_for_pay_and_drive/",views.get_all_my_extra_payment_for_pay_and_drive),
]