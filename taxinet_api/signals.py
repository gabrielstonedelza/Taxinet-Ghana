from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (ScheduleRide, Complains, ScheduledNotifications,  CancelScheduledRide,
                     Wallets, LoadWallet, UpdatedWallets,
                     RentACar,
                      )
from django.conf import settings

User = settings.AUTH_USER_MODEL

from taxinet_users.models import User


@receiver(post_save, sender=RentACar)
def alert_new_car_rent_request(sender, created, instance, **kwargs):
    title = "New Car Rent Request"
    notification_tag = "Rent Request"
    message = f"{instance.passenger.username} wants to rent a car"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.passenger,
                                              notification_to=instance.administrator,
                                              rent_car_id=instance.id,rent_car_title=instance.schedule_type
                                              )


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
                                              )


@receiver(post_save, sender=CancelScheduledRide)
def alert_cancelled_ride(sender, created, instance, **kwargs):
    title = "ScheduleRide Cancelled"
    notification_tag = "ScheduleRide Cancelled"
    message = f"{instance.passenger.username} has Cancelled ride '{instance.ride}'"
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
                                                  notification_to=instance.user)


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
                                                  notification_to=instance.user)


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
                                                  notification_to=instance.user)