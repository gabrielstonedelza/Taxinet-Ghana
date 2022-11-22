from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (ScheduleRide, Complains, ConfirmDriverPayment, AcceptedScheduledRides,
                     RejectedScheduledRides, DriverVehicleInventory,
                     CompletedScheduledRides, ScheduledNotifications, AssignScheduleToDriver,
                     AcceptAssignedScheduled, AddToUpdatedWallets,
                     RejectAssignedScheduled, CancelScheduledRide, PassengersWallet, AskToLoadWallet, DriverStartTrip,
                     DriverEndTrip, DriverAlertArrival, DriversWallet,
                     DriverAddToUpdatedWallets, DriverAskToLoadWallet, AddToPaymentToday, OtherWallet, WorkAndPay,
                     Wallets, LoadWallet, UpdatedWallets, ExpensesRequest, PrivateUserMessage, Stocks, MonthlySalary,
                     PayPromoterCommission, PrivateChatId, AddToBlockList, DriversCommission, DriverRequestCommission,
                     WalletAddition, WorkExtra, CallForInspection,
                     DriverTransferCommissionToWallet, WalletDeduction)
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
                                              notification_to=instance.scheduled_ride.passenger,
                                              schedule_ride_id=instance.scheduled_ride.id,
                                              schedule_ride_slug=instance.scheduled_ride.slug,
                                              )


@receiver(post_save, sender=RejectedScheduledRides)
def alert_rejected_ride(sender, created, instance, **kwargs):
    if created:
        title = "Ride was rejected"
        notification_tag = "Ride Rejected"
        message = f"{instance.administrator.username} rejected your ride."
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.ride.administrator,
                                              notification_to=instance.ride.passenger,
                                              ride_id=instance.ride.id, schedule_ride_slug=instance.ride.slug,
                                              )


@receiver(post_save, sender=CompletedScheduledRides)
def alert_completed_ride(sender, created, instance, **kwargs):
    title = "Your trip is completed"
    notification_tag = "Ride Completed"
    message = f"Your trip from {instance.scheduled_ride.pick_up} to {instance.scheduled_ride.drop_off} is now completed."
    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.scheduled_ride.administrator,
                                              notification_to=instance.scheduled_ride.passenger,
                                              ride_id=instance.ride.id)
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_tag=notification_tag, notification_message=message,
                                              notification_from=instance.scheduled_ride.administrator,
                                              notification_to=instance.scheduled_ride.assigned_driver,
                                              ride_id=instance.ride.id)


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


@receiver(post_save, sender=ExpensesRequest)
def alert_expense_request(sender, created, instance, **kwargs):
    title = "New Expense Request"
    notification_tag = "Expense Request"
    message = f"{instance.user.username} added a new expense report"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.user,
                                              notification_to=instance.guarantor, )


@receiver(post_save, sender=DriverVehicleInventory)
def alert_driver_inventory_today(sender, created, instance, **kwargs):
    title = "New driver inventory"
    notification_tag = "Inventory Check"
    message = f"{instance.driver.username} send his car's inventory for today"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.driver,
                                              notification_to=instance.administrator,
                                              drivers_inventory_id=instance.id)


@receiver(post_save, sender=AssignScheduleToDriver)
def alert_assigned_scheduled_to_driver(sender, created, instance, **kwargs):
    title = "New ride assigned"
    notification_tag = "Ride Assigned"
    message = f"'{instance.ride}' has been assigned to {instance.driver.username} "

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to=instance.passenger,
                                              assigned_scheduled_id=instance.id,
                                              schedule_ride_slug=instance.ride.slug,
                                              )
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to=instance.ride.assigned_driver,
                                              assigned_scheduled_id=instance.id,
                                              schedule_ride_slug=instance.ride.slug,
                                              )


@receiver(post_save, sender=AcceptAssignedScheduled)
def alert_accepted_assigned_scheduled_to_driver(sender, created, instance, **kwargs):
    title = "Ride assigned accepted"
    notification_tag = "Ride Accepted"
    message = f"{instance.driver.username} has accepted ride '{instance.assigned_to_driver.ride}'"
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
    message = f"{instance.driver.username} has rejected ride '{instance.assigned_to_driver.ride}'"
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


@receiver(post_save, sender=PassengersWallet)
def alert_loaded_wallet(sender, created, instance, **kwargs):
    title = "Wallet Loaded"
    notification_tag = "Wallet Loaded"
    message = f"{instance.passenger.username}, your wallet has been loaded with the amount of GHS{instance.amount}"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_from=instance.administrator,
                                              notification_to=instance.passenger)


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
                                              notification_to=instance.wallet.passenger)


@receiver(post_save, sender=AddToVerified)
def alert_added_to_verified(sender, created, instance, **kwargs):
    title = "Profile Verified"
    notification_tag = "Profile Verified"
    message = f"Hi {instance.user.user.username}, your account is verified successfully."

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.user.user)


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
    message = f"{instance.driver.username} has started trip {instance.ride}"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.administrator,
                                              )
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.passenger,
                                              )


@receiver(post_save, sender=DriverEndTrip)
def alert_driver_end_trip(sender, created, instance, **kwargs):
    title = "Trip Ended"
    notification_tag = "Trip Ended"
    message = f"{instance.driver.username} has ended trip {instance.ride}"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.administrator,
                                              )
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.passenger,
                                              )


@receiver(post_save, sender=DriverAlertArrival)
def driver_alert_arrival(sender, created, instance, **kwargs):
    title = "Driver Arrived"
    notification_tag = "Driver Arrived"
    message = f"{instance.driver.username} has arrived"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.passenger)


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
                                              notification_to=instance.administrator,
                                              )

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver,
                                              )


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


# new updates
@receiver(post_save, sender=PrivateUserMessage)
def alert_private_message(sender, created, instance, **kwargs):
    title = f"New private message"

    if created:
        if instance.sender:
            message = f"{instance.sender.username} sent you a message"
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message,
                                                  notification_to=instance.receiver)
        if instance.receiver:
            message = f"{instance.receiver.username} sent you a message"
            ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                                  notification_message=message,
                                                  notification_to=instance.sender)


@receiver(post_save, sender=AddToBlockList)
def alert_account_blocked(sender, created, instance, **kwargs):
    title = "Account Blocked"
    message = f"Your account was blocked by the administrator"
    notification_tag = "Account Blocked"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.user, notification_from=instance.administrator)


@receiver(post_save, sender=PayPromoterCommission)
def alert_promoter_commission(sender, created, instance, **kwargs):
    title = "Commission Payment"
    message = f"Your wallet was credited with {instance.amount}"
    notification_tag = "Commission Payment"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.promoter)


@receiver(post_save, sender=MonthlySalary)
def alert_promoter_commission(sender, created, instance, **kwargs):
    title = "Monthly Salary Payment"
    message = f"GHS{instance.amount} was deposited into your accounts"
    notification_tag = "Monthly Salary Payment"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver)


@receiver(post_save, sender=DriversCommission)
def alert_driver_commission(sender, created, instance, **kwargs):
    title = "Commission Received"
    message = f"You have received an amount of {instance.amount} as commission for your payment"
    notification_tag = "Commission Received"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver)


@receiver(post_save, sender=DriverRequestCommission)
def alert_driver_request_commission(sender, created, instance, **kwargs):
    title = "Commission redeem request"
    message = f"{instance.driver.username} wants to redeem commission worth of {instance.amount}"
    notification_tag = "Commission Received"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.administrator)

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.accounts)


@receiver(post_save, sender=DriverTransferCommissionToWallet)
def alert_driver_request_commission(sender, created, instance, **kwargs):
    title = "Commission to wallet"
    message = f"You have transferred {instance.amount} of your commission to your wallet"
    notification_tag = "Commission to wallet"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver)


@receiver(post_save, sender=WalletDeduction)
def alert_wallet_deducted(sender, created, instance, **kwargs):
    title = "Action on wallet"
    message = f"An amount of {instance.amount} was deducted from your wallet,reason is {instance.reason}"
    notification_tag = "Commission to wallet"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.user)


@receiver(post_save, sender=WalletAddition)
def alert_wallet_added(sender, created, instance, **kwargs):
    title = "Action on wallet"
    message = f"An amount of {instance.amount} was added to your wallet,reason is {instance.reason}"
    notification_tag = "Commission to wallet"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.user)


@receiver(post_save, sender=WorkExtra)
def alert_wallet_added(sender, created, instance, **kwargs):
    title = "Work Extra Activated"
    message = f"You have activated the work extra and an amount of ₵{instance.amount} has deducted from your wallet"

    message1 = f"{instance.driver.username} activated the work extra and an amount of ₵{instance.amount} has deducted from his wallet"
    notification_tag = "Work Extra Activated"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver)

        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message1, notification_tag=notification_tag,
                                              notification_to=instance.administrator)


@receiver(post_save, sender=CallForInspection)
def alert_called_for_inspection(sender, created, instance, **kwargs):
    title = "Called For Inspection"
    message = f"Please you are to report to Taxinet for on {instance.day_for_inspection} for vehicle inspection.Thank you."

    notification_tag = "Called For Inspection"

    if created:
        ScheduledNotifications.objects.create(notification_id=instance.id, notification_title=title,
                                              notification_message=message, notification_tag=notification_tag,
                                              notification_to=instance.driver)
