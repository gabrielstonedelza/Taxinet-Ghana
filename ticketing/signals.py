from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import Booking,AddToBooked
from users.models import User


@receiver(post_save,sender=Booking)
def alert_booking_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Flight Request"
        message = f"{instance.user.username} wants to book a flight from {instance.departure_airport} to {instance.arrival_airport} on {instance.departure_date} @ {instance.departure_time}."

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)


@receiver(post_save,sender=AddToBooked)
def alert_booked(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Flight Booked"
        message = f"Hi,{instance.user.username},your flight from {instance.booking.departure_airport} to {instance.booking.arrival_airport} on {instance.booking.departure_date} @ {instance.booking.departure_time} has been booked successfully.Full flight details has been sent to your email address.Have a safe and wonderful flight"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.user,notification_from=admin_user)