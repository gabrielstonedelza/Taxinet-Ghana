from django.urls import path
from . import views

urlpatterns = [
    path("profile/",views.get_my_profile),
    path("profile/<int:id>/update/",views.update_profile),
]