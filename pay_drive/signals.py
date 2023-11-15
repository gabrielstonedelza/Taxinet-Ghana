from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import RequestPayAndDrive, AddToApprovedPayAndDrive
from users.models import User


@receiver(post_save,sender=RequestPayAndDrive)
def alert_drive_pay_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Pay and Drive Request"
        message = f"{instance.user.username} is requesting Pay and Drive"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)


@receiver(post_save,sender=AddToApprovedPayAndDrive)
def alert_drive_pay_approved(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Pay and Drive Approved"
        message = f"Hi,{instance.user.username}, your pay and drive request has been approved."

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.user,notification_from=admin_user)