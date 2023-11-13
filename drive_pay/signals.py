from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import RequestDriveAndPay
from users.models import User


@receiver(post_save,sender=RequestDriveAndPay)
def alert_drive_pay_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Drive and Pay Request"
        message = f"{instance.user.username} is requesting Drive and Pay"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)