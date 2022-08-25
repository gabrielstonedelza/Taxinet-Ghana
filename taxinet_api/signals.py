from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (ScheduleRide, Complains, ConfirmDriverPayment, AcceptedScheduledRides,
                     RejectedScheduledRides, DriverVehicleInventory,
                     CompletedScheduledRidesToday, ScheduledNotifications, AssignScheduleToDriver,
                     AcceptAssignedScheduled, AddToUpdatedWallets,
                     RejectAssignedScheduled, CancelScheduledRide, PassengersWallet, AskToLoadWallet)
from django.conf import settings

User = settings.AUTH_USER_MODEL
from taxinet_users.models import User, AddToVerified


@receiver(post_save, sender=AcceptedScheduledRides)
def alert_accepted_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was accepted"
        notification_tag = "Ride Accepted"
        message = f"{instance.administrator.username} accepted your ride."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.scheduled_ride.administrator,
                                              notification_to_passenger=instance.scheduled_ride.passenger,
                                              schedule_ride_id=instance.scheduled_ride.id,
                                              schedule_ride_slug=instance.scheduled_ride.slug,
                                              schedule_ride_title=instance.scheduled_ride.schedule_title, )


@receiver(post_save, sender=RejectedScheduledRides)
def alert_rejected_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was rejected"
        notification_tag = "Ride Rejected"
        message = f"{instance.administrator.username} rejected your ride."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.ride.administrator,
                                              notification_to_passenger=instance.ride.passenger,
                                              ride_id=instance.ride.id, schedule_ride_slug=instance.ride.slug,
                                              schedule_ride_title=instance.scheduled_ride.schedule_title)


@receiver(post_save, sender=CompletedScheduledRidesToday)
def alert_completed_ride(sender, created, instance, **kwargs):
    if created:
        title = "Your trip is completed"
        notification_tag = "Ride Completed"
        message = f"Your trip from {instance.pick_up} to {instance.drop_off} is now completed."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.ride.administrator,
                                              notification_to_passenger=instance.ride.passenger,
                                              ride_id=instance.ride.id)


@receiver(post_save, sender=ScheduleRide)
def alert_schedule(sender, created, instance, **kwargs):
    title = "New Schedule Ride Request"
    notification_tag = "Schedule Request"
    message = f"{instance.passenger.username} wants schedule with you"
    admin_user = User.objects.get(id=1)

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.passenger,
                                              notification_to=instance.administrator,
                                              schedule_ride_id=instance.id, schedule_ride_slug=instance.slug,
                                              schedule_ride_title=instance.schedule_title, )


@receiver(post_save, sender=DriverVehicleInventory)
def alert_driver_inventory_today(sender, created, instance, **kwargs):
    title = "New driver inventory"
    notification_tag = "Inventory Check"
    message = f"{instance.driver.username} send his car's inventory for today"
    admin_user = User.objects.get(id=1)

    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.driver,
                                          notification_to=admin_user,
                                          drivers_inventory_id=instance.id)


@receiver(post_save, sender=AssignScheduleToDriver)
def alert_assigned_scheduled_to_driver(sender, created, instance, **kwargs):
    title = "New ride assigned"
    notification_tag = "Ride Assigned"
    message = f"'{instance.ride.schedule_title}' has been assigned to {instance.driver.username} "
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.administrator,
                                          notification_to=instance.driver,
                                          notification_to_passenger=instance.ride.passenger,
                                          assigned_scheduled_id=instance.id, schedule_ride_slug=instance.ride.slug,
                                          schedule_ride_title=instance.ride.schedule_title, )


@receiver(post_save, sender=AcceptAssignedScheduled)
def alert_accepted_assigned_scheduled_to_driver(sender, created, instance, **kwargs):
    title = "Ride assigned accepted"
    notification_tag = "Ride Accepted"
    message = f"{instance.driver.username} has accepted ride '{instance.assigned_to_driver.ride.schedule_title}'"
    admin_user = User.objects.get(id=1)
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.driver,
                                          notification_to=admin_user,
                                          accept_assigned_scheduled_id=instance.id)


@receiver(post_save, sender=RejectAssignedScheduled)
def alert_rejected_assigned_scheduled_to_driver(sender, created, instance, **kwargs):
    title = "Ride assigned rejected"
    notification_tag = "Ride Rejected"
    message = f"{instance.driver.username} has rejected ride '{instance.assigned_to_driver.ride.schedule_title}'"
    admin_user = User.objects.get(id=1)
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.driver,
                                          notification_to=admin_user,
                                          reject_assigned_scheduled_id=instance.id)


@receiver(post_save, sender=CancelScheduledRide)
def alert_cancelled_ride(sender, created, instance, **kwargs):
    title = "ScheduleRide Cancelled"
    notification_tag = "ScheduleRide Cancelled"
    message = f"{instance.passenger.username} has Cancelled ride '{instance.ride.schedule_title}'"
    admin_user = User.objects.get(id=1)
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.passenger,
                                          notification_to=admin_user)


@receiver(post_save, sender=PassengersWallet)
def alert_loaded_wallet(sender, created, instance, **kwargs):
    title = "Wallet Loaded"
    notification_tag = "Wallet Loaded"
    message = f"{instance.passenger.username}, your wallet has been loaded with the amount of GHS{instance.amount}"
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.administrator,
                                          notification_to_passenger=instance.passenger)


@receiver(post_save, sender=AskToLoadWallet)
def alert_request_to_load_wallet(sender, created, instance, **kwargs):
    title = "Wants to load wallet"
    notification_tag = "Wants to load wallet"
    message = f"{instance.passenger.username} wants to load their wallet with the amount of GHS{instance.amount}"
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.passenger,
                                          notification_to=instance.administrator)


@receiver(post_save, sender=AddToUpdatedWallets)
def alert_updated_wallet(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.passenger.username}, your wallet was updated with GHS {instance.wallet.amount}"
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_from=instance.administrator,
                                          notification_to_passenger=instance.wallet.passenger)


@receiver(post_save, sender=AddToVerified)
def alert_added_to_verified(sender, created, instance, **kwargs):
    title = "Profile Verified"
    notification_tag = "Profile Verified"
    message = f"Hi {instance.user.username}, your account is verified successfully."
    ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                          notification_message=message, notification_tag=notification_tag,
                                          notification_to_passenger=instance.user)
