from django.urls import path
from . import views

urlpatterns = [
    path("profile/",views.get_my_profile),
    path("profile/update/",views.update_profile),
]