from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import RequestDriveAndPay,AddToApprovedDriveAndPay
from users.models import User


@receiver(post_save,sender=RequestDriveAndPay)
def alert_drive_pay_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Drive and Pay Request"
        message = f"{instance.user.username} is requesting Drive and Pay"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)

@receiver(post_save,sender=AddToApprovedDriveAndPay)
def alert_drive_pay_approved(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Drive and Pay Approved"
        message = f"Hi,{instance.user.username}, your drive and pay request has been approved."

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.user,notification_from=admin_user)