from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ReferralWallets


@receiver(post_save, sender=ReferralWallets)
def create_referral_wallets(sender, created, instance, **kwargs):
    if created:
        ReferralWallets.objects.create(referral=instance)
