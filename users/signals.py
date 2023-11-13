from django.db.models.signals import post_save
from django.dispatch import receiver
from profiles.models import Profile
from users.models import User
from wallets.models import Wallets


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        Wallets.objects.create(user=instance)