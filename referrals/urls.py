from django.urls import path

from . import views

urlpatterns = [
    path("add_new_referral/", views.add_new_referral),
    path("get_all_referrals/", views.get_all_referrals),
    path("create_referrals_wallet/", views.create_referrals_wallet),
    path("get_all_referrals_wallets/", views.get_all_referrals_wallets),
    path("get_all_referrals_updated_wallets/", views.get_all_referrals_updated_wallets),
    path("update_referral_wallet/<int:id>/<str:amount_to_update>/", views.update_referral_wallet),
    path("delete_referral/<int:id>/", views.delete_referral),
    path("referral_wallet/<int:id>/<str:amount>/update/",views.update_referral_wallet_wallet),
]