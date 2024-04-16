from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Referrals, ReferralWallets


@receiver(post_save,sender=Referrals)
def alert_referral_wallet_created(sender,created,instance,**kwargs):
    if created:
        ReferralWallets.objects.create(referral=instance)