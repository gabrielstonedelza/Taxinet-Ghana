from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DriverProfile, PassengerProfile
from django.conf import settings

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created and instance.user_type == "Driver":
        DriverProfile.objects.create(user=instance)

    if created and instance.user_type == "Passenger":
        PassengerProfile.objects.create(user=instance)