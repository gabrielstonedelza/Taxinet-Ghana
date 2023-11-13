from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import Booking
from users.models import User


@receiver(post_save,sender=Booking)
def alert_booking(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Flight Booked"
        message = f"Hi,{instance.user.username},your flight from {instance.departure_airport} to {instance.arrival_airport} on {instance.departure_date} @ {instance.departure_time} has been booked successfully.Full flight details has been sent to your email address.Have a safe and wonderful flight"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.user,notification_from=admin_user)