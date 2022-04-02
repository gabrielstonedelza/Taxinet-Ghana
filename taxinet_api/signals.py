from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import (RequestRide, AcceptRide, ScheduleRide, AcceptScheduleRide, Notifications, Complains, DriverReviews, \
                     Sos, RateDriver, ConfirmDriverPayment)

User = settings.AUTH_USER_MODEL
from taxinet_users.models import User as taxinet_user
from taxinet_users.models import DriverProfile, PassengerProfile


@receiver(post_save, sender=RequestRide)
def alert_request_ride(sender, created, instance, **kwargs):
    title = "New Ride Request"
    notification_tag = "Ride Request"
    message = f"{instance.passenger.username} is requesting a ride from you."

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag, notification_message=message,
                                     notification_from=instance.passenger, notification_to=instance.driver,
                                     ride_id=instance.id)


@receiver(post_save, sender=AcceptRide)
def alert_accepted_ride(sender, created, instance, **kwargs):
    title = "Ride Request Accepted"
    notification_tag = "Ride Accepted"
    message = f"{instance.ride.driver.username} accepted your request and added your fare,please check and feel free to bargain."

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag,
                                     notification_message=message, notification_from=instance.ride.driver,
                                     notification_to=instance.ride.passenger, ride_accepted_id=instance.id)


@receiver(post_save, sender=AcceptRide)
def alert_rejected_ride(sender, created, instance, **kwargs):
    title = "Ride Request Rejected"
    notification_tag = "Ride Rejected"
    message = f"{instance.ride.driver.username} rejected your request"

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag,
                                     notification_message=message, notification_from=instance.ride.driver,
                                     notification_to=instance.ride.passenger, ride_rejected_id=instance.id)


@receiver(post_save, sender=AcceptRide)
def alert_bidding(sender, created, instance, **kwargs):
    if created and instance.ride.passenger == instance.user:
        title = "Passenger bid on the price"
        notification_tag = "Bidding"
        message = f"{instance.ride.passenger.username} has offered to pay {instance.bid}"
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.ride.passenger, notification_to=instance.ride.driver,
                                     ride_accepted_id=instance.id)

    if created and instance.ride.driver == instance.user:
        title = "Driver bid on the price"
        notification_tag = "Bidding"
        message = f"{instance.ride.driver.username} bid on the fare {instance.bid}"
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.ride.driver, notification_to=instance.ride.passenger,
                                     ride_accepted_id=instance.id)

    if created and instance.driver_approved == "Approved":
        title = "Price Approved"
        notification_tag = "Price Approved"
        message = "Driver approved price"

        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.user, notification_to=instance.ride.passenger,
                                     ride_accepted_id=instance.id)

    if created and instance.passenger_approved == "Approved":
        title = "Price Approved"
        notification_tag = "Price Approved"
        message = "Passenger also approved price"

        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.user, notification_to=instance.ride.driver,
                                     ride_accepted_id=instance.id)

    if created and instance.passenger_approved == "Approved" and instance.driver_approved == "Approved":
        title = "Price Finally Approved"
        notification_tag = "Final Price Approved"
        message = f"Both of you have approved {instance.price}"

        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.ride.passenger, notification_to=instance.ride.driver,
                                     ride_accepted_id=instance.id)


@receiver(post_save, sender=ScheduleRide)
def alert_schedule(sender, created, instance, **kwargs):
    title = "New Schedule Ride Request"
    notification_tag = "Schedule Request"
    message = f"{instance.passenger.username} wants schedule with you"

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.passenger, notification_to=instance.driver,
                                     schedule_ride_id=instance.id)


@receiver(post_save, sender=AcceptScheduleRide)
def alert_schedule_accepted(sender, created, instance, **kwargs):
    title = "Schedule Ride Request Accepted"
    notification_tag = "Schedule Ride Accepted"
    message = f"{instance.driver.username} accepted your request and would be calling you."

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag,
                                     notification_message=message, notification_from=instance.user,
                                     notification_to=instance.scheduled_ride.passenger, ride_accepted_id=instance.id)


@receiver(post_save, sender=DriverReviews)
def alert_review(sender, created, instance, **kwargs):
    title = "Got a new review"
    notification_tag = "Driver Review"
    message = f"{instance.passenger.username} wrote a review about you."

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.user, notification_to=instance.driver,
                                     review_id=instance.id)


@receiver(post_save, sender=RateDriver)
def alert_rating(sender, created, instance, **kwargs):
    title = "New Rating for you"
    notification_tag = "Rating"
    message = f"{instance.passenger.username} gave you a rating of {instance.rating}"

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.passenger, notification_to=instance.driver,
                                     rating_id=instance.id)


@receiver(post_save, sender=ConfirmDriverPayment)
def alert_payment_confirmed(sender, created, instance, **kwargs):
    title = "Payment confirmation"
    notification_tag = "Payment Confirmed"
    message = f"Your payment of GH{instance.amount} has been confirmed"
    admin_user = taxinet_user.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=admin_user, notification_to=instance.driver,
                                     payment_confirmed_id=instance.id)


@receiver(post_save, sender=Complains)
def alert_complains(sender, created, instance, **kwargs):
    title = "New Complain"
    notification_tag = "Complains"
    message = f"{instance.complainant.username} just complained about {instance.offender}"
    admin_user = taxinet_user.objects.get(id=1)

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.complainant, notification_to=admin_user,
                                     complain_id=instance.id)
