from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import (RequestRide, BidRide, ScheduleRide, BidScheduleRide, Notifications, Complains, DriverReviews, \
                     Sos, DriversPoints, ConfirmDriverPayment, RejectedRides, AcceptedRides,CompletedRides,CompletedBidOnRide)

User = settings.AUTH_USER_MODEL
from taxinet_users.models import User as taxinet_user
from taxinet_users.models import DriverProfile, PassengerProfile


@receiver(post_save, sender=RequestRide)
def alert_request_ride(sender, created, instance, **kwargs):
    if created:
        title = "New Ride Request"
        notification_tag = "Ride Request"
        message = f"{instance.passenger.username} is requesting a ride from you."
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag, notification_message=message,
                                     notification_from=instance.passenger, notification_to=instance.driver,
                                     ride_id=instance.id, pick_up_place_id=instance.passengers_pick_up_place_id,
                                     drop_off_place_id=instance.passengers_drop_off_place_id,
                                     passengers_lat=instance.passengers_lat, passengers_lng=instance.passengers_lng,
                                     passengers_pickup=instance.pick_up, passengers_dropff=instance.drop_off,
                                     ride_duration=instance.ride_duration, ride_distance=instance.ride_distance,
                                     drivers_lat=instance.drivers_lat, drivers_lng=instance.drivers_lng)


@receiver(post_save, sender=AcceptedRides)
def alert_accepted_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was accepted"
        notification_tag = "Ride Accepted"
        message = f"{instance.driver.username} accepted your ride."
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag, notification_message=message,
                                     notification_from=instance.ride.driver, notification_to=instance.ride.passenger,
                                     ride_id=instance.ride.id)

@receiver(post_save, sender=RejectedRides)
def alert_rejected_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was rejected"
        notification_tag = "Ride Rejected"
        message = f"{instance.driver.username} rejected your ride."
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag, notification_message=message,
                                     notification_from=instance.ride.driver, notification_to=instance.ride.passenger,
                                     ride_id=instance.ride.id)


@receiver(post_save, sender=CompletedBidOnRide)
def alert_completed_bid_on_ride(sender, created, instance, **kwargs):
    if created:
        title = "Bidding was accepted and now complete"
        notification_tag = "Bid Completed"
        message = f"{instance.driver.username} accepted bid and now complete."
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag, notification_message=message,
                                     notification_from=instance.ride.driver, notification_to=instance.ride.passenger,
                                     ride_id=instance.ride.id)

@receiver(post_save, sender=CompletedRides)
def alert_completed_ride(sender, created, instance, **kwargs):
    if created:
        title = "Your trip is completed"
        notification_tag = "Ride Completed"
        message = f"Your trip from {instance.pick_up} to {instance.drop_off} is now completed."
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_tag=notification_tag, notification_message=message,
                                     notification_from=instance.ride.driver, notification_to=instance.ride.passenger,
                                     ride_id=instance.ride.id)


@receiver(post_save, sender=BidRide)
def alert_bidding(sender, created, instance, **kwargs):
    if created and instance.ride.passenger == instance.user:
        title = "New bid on price"
        notification_tag = "Bidding"
        message = f"{instance.user.username} has offered to pay {instance.bid}"
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.ride.passenger, notification_to=instance.ride.driver,
                                     ride_accepted_id=instance.id)

    if created and instance.ride.driver == instance.user:
        title = "New bid on price"
        notification_tag = "Bidding"
        message = f"{instance.user.username} wants you to pay {instance.bid}"
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.ride.driver, notification_to=instance.ride.passenger,
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


@receiver(post_save, sender=BidScheduleRide)
def alert_bidding(sender, created, instance, **kwargs):
    if created and instance.scheduled_ride.passenger == instance.user:
        title = "New bid on price"
        notification_tag = "Bidding"
        message = f"{instance.user.username} has offered to pay {instance.bid}"
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.scheduled_ride.passenger,
                                     notification_to=instance.scheduled_ride.driver,
                                     schedule_accepted_id=instance.id)

    if created and instance.scheduled_ride.driver == instance.user:
        title = "New bid on price"
        notification_tag = "Bidding"
        message = f"{instance.user.username} wants you to pay {instance.bid}"
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.scheduled_ride.driver,
                                     notification_to=instance.scheduled_ride.passenger,
                                     schedule_accepted_id=instance.id)


@receiver(post_save, sender=DriverReviews)
def alert_review(sender, created, instance, **kwargs):
    title = "Got a new review"
    notification_tag = "Driver Review"
    message = f"{instance.passenger.username} wrote a review about you."

    if created:
        Notifications.objects.create(notification_id=instance.id, notification_title=title,
                                     notification_message=message, notification_tag=notification_tag,
                                     notification_from=instance.passenger, notification_to=instance.driver,
                                     review_id=instance.id)


@receiver(post_save, sender=DriversPoints)
def alert_rating(sender, created, instance, **kwargs):
    title = "New Rating for you"
    notification_tag = "Rating"
    message = f"{instance.passenger.username} gave you a rating of {instance.points}"

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
