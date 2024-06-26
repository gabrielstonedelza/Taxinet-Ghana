from django.urls import path
from . import views

urlpatterns = [
    path("get_all_wallets/",views.get_all_wallets),
    path("get_my_wallet/",views.get_my_wallet),
    path("get_my_updated_wallet/",views.get_my_updated_wallet),
    path("get_users_updated_wallet/<int:id>/",views.get_users_updated_wallet),
    path("wallet/<int:id>/<str:amount>/update/",views.update_wallet),
    path("wallet/<int:id>/add/",views.add_to_updated_wallet),
]