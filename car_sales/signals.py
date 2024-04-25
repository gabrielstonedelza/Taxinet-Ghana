from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import Vehicle, AddCarImage, BuyVehicle, AddToApprovedVehiclePurchases
from users.models import User


@receiver(post_save,sender=BuyVehicle)
def alert_delivery_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Vehicle Purchase Request"
        message = f"{instance.user.username} wants to purchase {instance.vehicle.name}"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)


@receiver(post_save,sender=AddToApprovedVehiclePurchases)
def alert_purchase_request_approved(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Vehicle Purchase Request Approved"
        message = f"Hi,{instance.user.username}, your request to purchase {instance.vehicle.name} has been approved"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=instance.user,notification_from=admin_user)


@receiver(post_save,sender=Vehicle)
def alert_new_vehicle(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        users = User.objects.exclude(id=1)
        title = "New Vehicle Added"
        message = "Hey hi, Taxinet added a new vehicle to their collection"
        for i in users:
            Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=i,notification_from=admin_user)
