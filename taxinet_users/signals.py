from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (DriverProfile, PassengerProfile, AdministratorsProfile, InvestorsProfile, AddToVerified, BigTrucksAdminProfile, RideAdminProfile, PromoterProfile, AccountsProfile)
from django.conf import settings
from taxinet_api.models import Wallets

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created and instance.user_type == "Driver":
        DriverProfile.objects.create(user=instance)

    if created and instance.user_type == "Passenger":
        PassengerProfile.objects.create(user=instance)

    if created and instance.user_type == "Investor":
        InvestorsProfile.objects.create(user=instance)

    if created and instance.user_type == "Administrator":
        AdministratorsProfile.objects.create(user=instance)

    if created and instance.user_type == "Accounts":
        AccountsProfile.objects.create(user=instance)

    if created and instance.user_type == "Promoter":
        PromoterProfile.objects.create(user=instance)

    if created and instance.user_type == "RideAdmin":
        RideAdminProfile.objects.create(user=instance)

    if created and instance.user_type == "BigTrucksAdmin":
        BigTrucksAdminProfile.objects.create(user=instance)

    if created:
        Wallets.objects.create(user=instance)
