from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (ScheduleRide, BidScheduleRide, Complains, ConfirmDriverPayment, Messages, AcceptedScheduledRides,
                     RejectedScheduledRides, BidScheduleRide, CompletedBidOnScheduledRide, DriverVehicleInventory,
                     CompletedScheduledRides, ScheduledNotifications)
from django.conf import settings

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=AcceptedScheduledRides)
def alert_accepted_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was accepted"
        notification_tag = "Ride Accepted"
        message = f"{instance.driver.username} accepted your ride."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.scheduled_ride.driver,
                                              notification_to=instance.scheduled_ride.passenger,
                                              schedule_ride_id=instance.scheduled_ride.id, )


@receiver(post_save, sender=RejectedScheduledRides)
def alert_rejected_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was rejected"
        notification_tag = "Ride Rejected"
        message = f"{instance.driver.username} rejected your ride."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.ride.driver,
                                              notification_to=instance.ride.passenger,
                                              ride_id=instance.ride.id)


@receiver(post_save, sender=CompletedBidOnScheduledRide)
def alert_completed_bid_on_ride(sender, created, instance, **kwargs):
    if created:
        title = "Bidding Accepted"
        notification_tag = "Bid Completed"
        message = f"{instance.driver.username} accepted bid and now complete."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.ride.driver,
                                              notification_to=instance.ride.passenger,
                                              drivers_lat=instance.drivers_lat, drivers_lng=instance.drivers_lng,
                                              ride_id=instance.ride.id, passengers_pickup=instance.ride.pick_up,
                                              pick_up_place_id=instance.ride.passengers_pick_up_place_id,
                                              passengers_lat=instance.ride.passengers_lat,
                                              passengers_lng=instance.ride.passengers_lng
                                              )


@receiver(post_save, sender=CompletedScheduledRides)
def alert_completed_ride(sender, created, instance, **kwargs):
    if created:
        title = "Your trip is completed"
        notification_tag = "Ride Completed"
        message = f"Your trip from {instance.pick_up} to {instance.drop_off} is now completed."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.ride.driver,
                                              notification_to=instance.ride.passenger,
                                              ride_id=instance.ride.id)


@receiver(post_save, sender=Messages)
def alert_received_message(sender, created, instance, **kwargs):
    if created and instance.ride.passenger == instance.user:
        title = "New message"
        notification_tag = "Messaging"
        message = f"{instance.user.username} sent you a message"
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.ride.passenger,
                                              notification_to=instance.ride.driver,
                                              message_id=instance.id)

    if created and instance.ride.driver == instance.user:
        title = "New message"
        notification_tag = "Messaging"
        message = f"{instance.user.username} sent you a message"
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.ride.driver,
                                              notification_to=instance.ride.passenger,
                                              message_id=instance.id)


@receiver(post_save, sender=ScheduleRide)
def alert_schedule(sender, created, instance, **kwargs):
    title = "New Schedule Ride Request"
    notification_tag = "Schedule Request"
    message = f"{instance.passenger.username} wants schedule with you"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.passenger, notification_to=instance.driver,
                                              schedule_ride_id=instance.id)


@receiver(post_save, sender=BidScheduleRide)
def alert_bidding(sender, created, instance, **kwargs):
    if created and instance.scheduled_ride.passenger == instance.user:
        title = "New bid on price"
        notification_tag = "Bidding"
        message = f"{instance.user.username} has offered to pay {instance.bid}"
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.scheduled_ride.passenger,
                                              notification_to=instance.scheduled_ride.driver,
                                              schedule_accepted_id=instance.id)

        if created and instance.scheduled_ride.driver == instance.user:
            title = "New bid on price"
            notification_tag = "Bidding"
            message = f"{instance.user.username} wants you to pay {instance.bid}"
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_from=instance.scheduled_ride.driver,
                                                  notification_to=instance.scheduled_ride.passenger,
                                                  schedule_ride_accepted_id=instance.id)
