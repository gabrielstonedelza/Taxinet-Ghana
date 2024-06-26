from django.urls import path
from . import views

urlpatterns = [
    path("request_drive_and_pay/<int:id>/",views.request_drive_and_pay),
    path("get_my_drive_and_pay_requests/",views.get_my_drive_and_pay_requests),
    path("get_all_drive_and_pay_requests/",views.get_all_drive_and_pay_requests),
    path("delete_drive_and_pay/<int:id>/",views.delete_drive_and_pay),
    path("update_approve_drive_drive/<int:pk>/",views.update_approve_drive_drive),
    path("add_to_drive_and_pay_complete/<int:id>/", views.add_to_drive_and_pay_complete),
    path("get_all_my_approved_drive_and_pay/", views.get_all_my_approved_drive_and_pay),
    path("get_all_approved_drive_and_pay/", views.get_all_approved_drive_and_pay),
    path("lock_car/", views.lock_car),
    path("add_to_drive_and_pay_daily/", views.add_to_drive_and_pay_daily),
    path("get_all_my_daily_payments_for_drive_and_pay/", views.get_all_my_daily_payments_for_drive_and_pay),
]