from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import UpdatedWallets,Wallets
from users.models import User


@receiver(post_save,sender=UpdatedWallets)
def alert_wallet_updated(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Wallet Updated"
        message = f"Hi {instance.wallet.user.username} ,your wallet was updated"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.wallet.user,notification_from=admin_user)