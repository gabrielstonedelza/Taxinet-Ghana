from django.urls import path

from . import views

urlpatterns = [
    path("my_notifications/",views.get_my_notifications),
    path("get_my_unread_notifications/",views.get_my_unread_notifications),
    path("get_triggered_notifications/",views.get_triggered_notifications),
    path("read_notification/",views.read_notification),
    path("un_trigger_notification/<int:id>/",views.un_trigger_notification),
    path("notification_detail/<int:id>/",views.get_notification_detail),
]