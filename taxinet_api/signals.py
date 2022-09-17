from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (ScheduleRide, Complains, ConfirmDriverPayment, AcceptedScheduledRides,
                     RejectedScheduledRides, DriverVehicleInventory,
                     CompletedScheduledRides, ScheduledNotifications, AssignScheduleToDriver,
                     AcceptAssignedScheduled, AddToUpdatedWallets,
                     RejectAssignedScheduled, CancelScheduledRide, PassengersWallet, AskToLoadWallet, DriverStartTrip,
                     DriverEndTrip, DriverAlertArrival, DriversWallet,
                     DriverAddToUpdatedWallets, DriverAskToLoadWallet, AddToPaymentToday, OtherWallet, WorkAndPay,
                     Wallets, LoadWallet, UpdatedWallets, RideMessages)
from django.conf import settings

User = settings.AUTH_USER_MODEL
from taxinet_users.models import User, AddToVerified, AddCardsUploaded


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


@receiver(post_save, sender=CompletedScheduledRides)
def alert_completed_ride(sender, created, instance, **kwargs):
    if created:
        title = "Your trip is completed"
        notification_tag = "Ride Completed"
        message = f"Your trip from {instance.scheduled_ride.pick_up} to {instance.scheduled_ride.drop_off} is now completed."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.scheduled_ride.administrator,
                                              notification_to_passenger=instance.scheduled_ride.passenger,
                                              ride_id=instance.ride.id,
                                              notification_to=instance.scheduled_ride.assigned_driver)


@receiver(post_save, sender=ScheduleRide)
def alert_schedule(sender, created, instance, **kwargs):
    title = "New Schedule Ride Request"
    notification_tag = "Schedule Request"
    message = f"{instance.passenger.username} wants schedule with you"

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

    if created:
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

    if created:
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

    if created:
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

    if created:
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

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.passenger,
                                              notification_to=admin_user)


@receiver(post_save, sender=Wallets)
def alert_loaded_wallet(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.user.username}, your wallet has been loaded with the amount of GHS{instance.amount}"

    if created:
        if instance.user.user_type == "Driver":
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to=instance.user)
        if instance.user.user_type == "Passenger":
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to_passenger=instance.user)


@receiver(post_save, sender=LoadWallet)
def request_to_load_wallet(sender, created, instance, **kwargs):
    title = "Wants to load wallet"
    notification_tag = "Wants to load wallet"
    message = f"{instance.user.username} wants to load their wallet with the amount of GHS{instance.amount}"

    if created:
        if instance.user.user_type == "Driver":
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to=instance.user)
        if instance.user.user_type == "Passenger":
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to_passenger=instance.user)


@receiver(post_save, sender=UpdatedWallets)
def updated_wallet(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.user.username}, your wallet was updated with GHS {instance.wallet.amount}"

    if created:
        if instance.user.user_type == "Driver":
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to=instance.user)
        if instance.user.user_type == "Passenger":
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to_passenger=instance.user)


@receiver(post_save, sender=PassengersWallet)
def alert_loaded_wallet(sender, created, instance, **kwargs):
    title = "Wallet Loaded"
    notification_tag = "Wallet Loaded"
    message = f"{instance.passenger.username}, your wallet has been loaded with the amount of GHS{instance.amount}"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to_passenger=instance.passenger)


@receiver(post_save, sender=AskToLoadWallet)
def alert_request_to_load_wallet(sender, created, instance, **kwargs):
    title = "Wants to load wallet"
    notification_tag = "Wants to load wallet"
    message = f"{instance.passenger.user.username} wants to load their wallet with the amount of GHS{instance.amount}"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.passenger.user,
                                              notification_to=instance.administrator)


@receiver(post_save, sender=AddToUpdatedWallets)
def alert_updated_wallet(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.passenger.username}, your wallet was updated with GHS {instance.wallet.amount}"

    if created:

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to_passenger=instance.wallet.passenger)


@receiver(post_save, sender=AddToVerified)
def alert_added_to_verified(sender, created, instance, **kwargs):
    title = "Profile Verified"
    notification_tag = "Profile Verified"
    message = f"Hi {instance.user.user.username}, your account is verified successfully."

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to_passenger=instance.user.user)


@receiver(post_save, sender=AddCardsUploaded)
def alert_cards_uploaded(sender, created, instance, **kwargs):
    title = "Cards Uploaded"
    notification_tag = "Cards Uploaded"
    message = f"{instance.user.user.username} has uploaded Ghana card."
    admin_user = User.objects.get(id=1)

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=admin_user)


@receiver(post_save, sender=DriverStartTrip)
def alert_driver_start_trip(sender, created, instance, **kwargs):
    title = "Trip Started"
    notification_tag = "Trip Started"
    message = f"{instance.driver.username} has started trip"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to_passenger=instance.passenger)


@receiver(post_save, sender=DriverEndTrip)
def alert_driver_end_trip(sender, created, instance, **kwargs):
    title = "Trip Ended"
    notification_tag = "Trip Ended"
    message = f"{instance.driver.username} has ended trip"

    if created:

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to_passenger=instance.passenger)


@receiver(post_save, sender=DriverAlertArrival)
def driver_alert_arrival(sender, created, instance, **kwargs):
    title = "Driver Arrived"
    notification_tag = "Driver Arrived"
    message = f"{instance.driver.username} has arrived"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to_passenger=instance.passenger)


@receiver(post_save, sender=DriversWallet)
def alert_drivers_loaded_wallet(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.driver.username}, your wallet has been updated.Wallet is now GHS{instance.amount}"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to=instance.driver)


@receiver(post_save, sender=DriverAskToLoadWallet)
def alert_drivers_request_to_load_wallet(sender, created, instance, **kwargs):
    title = "Wants to load wallet"
    notification_tag = "Wants to load wallet"
    message = f"{instance.driver.user.username} wants to load their wallet with the amount of GHS{instance.amount}"

    if created:

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.driver.user,
                                              notification_to=instance.administrator)


@receiver(post_save, sender=DriverAddToUpdatedWallets)
def alert_driver_updated_wallet(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.driver.username}, your wallet was updated with GHS {instance.wallet.amount}"

    if created:

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to=instance.wallet.driver)


@receiver(post_save, sender=AddToPaymentToday)
def alert_driver_payment_Today(sender, created, instance, **kwargs):
    title = "Payment Today"
    notification_tag = "Payment Today"
    message = f"70 GHS was deducted from your wallet.Your wallet is now {instance.amount}"

    if created:

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver)


@receiver(post_save, sender=OtherWallet)
def alert_wallet_transfer(sender, created, instance, **kwargs):
    title = "Wallet Updated"
    notification_tag = "Wallet Updated"
    message = f"{instance.sender.username} just sent GHS{instance.amount} to your wallet"

    if created:

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.receiver, )


@receiver(post_save, sender=WorkAndPay)
def alert_added_to_work_and_pay(sender, created, instance, **kwargs):
    title = "Added to work and pay"
    notification_tag = "Added to work and pay"
    message = f"You have been added to work and pay system"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver, )


@receiver(post_save, sender=RideMessages)
def alert_ride_message(sender, created, instance, **kwargs):
    if created:
        title = 'New ride message'
        notification_tag = "New ride message"
        message = f"Got new message for ride {instance.ride.schedule_title}"

        if instance.driver:
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to_passenger=instance.passenger,
                                                  notification_from=instance.driver)
        if instance.passenger:
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message, notification_tag=notification_tag,
                                                  notification_to=instance.driver, notification_from=instance.passenger)
