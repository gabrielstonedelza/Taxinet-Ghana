from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ScheduleRide
from notifications.models import Notifications

from users.models import User

@receiver(post_save, sender=ScheduleRide)
def alert_schedule(sender, created, instance, **kwargs):
    title = "New Schedule Ride Request"
    message = f"{instance.user.username} wants to schedule with you"
    admin_user = User.objects.get(id=1)

    if created:
        Notifications.objects.create(item_id=instance.id, notification_title=title,
                                              notification_message=message,
                                              notification_from=instance.user,
                                              notification_to=admin_user
                                              )
