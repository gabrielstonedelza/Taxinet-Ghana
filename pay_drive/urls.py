from django.urls import path

from . import views

urlpatterns = [
    path("request_pay_and_drive/",views.request_pay_and_drive),
    path("get_my_pay_and_drive_requests/",views.get_my_pay_and_drive_requests),
    path("get_all_pay_and_drive_requests/",views.get_all_pay_and_drive_requests),
    path("delete_pay_and_drive/<int:id>",views.delete_pay_and_drive),
]