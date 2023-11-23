from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import RequestDriveAndPay,AddToApprovedDriveAndPay, LockCarForTheDay
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


@receiver(post_save,sender=LockCarForTheDay)
def alert_car_locked(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Car Locked"
        message1 = f"{instance.user.username} just locked the car for the day."
        message2 = f"Hi there {instance.user.username}, you just received {instance.points} for locking your car."

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message1,notification_to=admin_user,notification_from=instance.user)
        Notifications.objects.create(item_id=instance.id, notification_title=title, notification_message=message2,
                                     notification_to=instance.user, notification_from=admin_user)