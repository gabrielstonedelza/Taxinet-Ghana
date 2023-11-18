from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from users.models import User
from .models import DriverVehicleInventory


@receiver(post_save,sender=DriverVehicleInventory)
def alert_driver_inventory(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "New Vehicle Inventory"
        message = f"{instance.user.username} has added his inventory for today"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)