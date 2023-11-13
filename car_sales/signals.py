from django.db.models.signals import post_save
from django.dispatch import receiver
from notifications.models import Notifications
from .models import Vehicle, AddCarImage, BuyVehicle
from users.models import User


@receiver(post_save,sender=BuyVehicle)
def alert_delivery_request(sender,created,instance,**kwargs):
    if created:
        admin_user = User.objects.get(id=1)
        title = "Vehicle Purchase Request"
        message = f"{instance.user.username} wants to purchase {instance.vehicle.name}"

        Notifications.objects.create(item_id=instance.id,notification_title=title,notification_message=message,notification_to=admin_user,notification_from=instance.user)