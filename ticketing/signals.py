from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import Booking,RequestBooking
from users.models import User


@receiver(post_save,sender=RequestBooking)
def alert_booking_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Flight Request"
        message = f"{instance.user.username} wants to book a flight from {instance.flight.departure_airport} to {instance.flight.arrival_airport} on {instance.flight.departure_date} @ {instance.flight.departure_time}."

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)


@receiver(post_save,sender=Booking)
def alert_booked(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Flight Booked"
        message = f"Hi,{instance.user.username},your flight from {instance.flight.departure_airport} to {instance.flight.arrival_airport} on {instance.flight.departure_date} @ {instance.flight.departure_time} has been booked successfully.Full flight details has been sent to your email address.Have a safe and wonderful flight"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.user,notification_from=admin_user)