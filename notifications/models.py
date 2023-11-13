from django.db import models

from users.models import User

NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)

class Notifications(models.Model):
    item_id = models.CharField(max_length=100, blank=True, default="")
    notification_title = models.CharField(max_length=200, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=100, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_receiving_notification", null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

