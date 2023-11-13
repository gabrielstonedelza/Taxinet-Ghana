from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import RequestPayAndDrive
from users.models import User


@receiver(post_save,sender=RequestPayAndDrive)
def alert_drive_pay_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Pay and Drive Request"
        message = f"{instance.user.username} is requesting Pay and Drive"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)