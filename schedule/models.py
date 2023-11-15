from django.db import models
from users.models import User

SCHEDULE_RIDE_OPTIONS = (
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Days", "Days"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
)

SCHEDULE_TYPES = (
    ("School Pick up And Drop Off", "School Pick up And Drop Off"),
    ("Office Pick up And Drop Off", "Office Pick up And Drop Off"),
    ("Airport Pick up And Drop Off", "Airport Pick up And Drop Off"),
    ("Delivery Pick up And Drop Off", "Delivery Pick up And Drop Off"),
    ("Hotel Pick up And Drop Off", "Hotel Pick up And Drop Off"),
)

SCHEDULE_PRIORITY = (
    ("High", "High"),
    ("Low", "Low"),
)
SCHEDULE_STATUS = (
    ("Pending", "Pending"),
    ("Active", "Active"),
    ("Cancelled", "Cancelled"),
)

SCHEDULE_DURATION = (
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Days", "Days"),
)


class ScheduleRide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_scheduling_ride")
    schedule_type = models.CharField(max_length=255, default="Airport Pick up And Drop Off", choices=SCHEDULE_TYPES)
    schedule_duration = models.CharField(max_length=255, default="One Time", choices=SCHEDULE_DURATION)
    pickup_location = models.CharField(max_length=255, blank=True, default="")
    drop_off_location = models.CharField(max_length=255, blank=True, default="")
    pick_up_time = models.CharField(max_length=100, blank=True, )
    start_date = models.CharField(max_length=100, blank=True, )
    completed = models.BooleanField(default=False)
    days = models.CharField(max_length=15, blank=True, default="")
    status = models.CharField(max_length=50, choices=SCHEDULE_STATUS, default="Pending")
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    charge = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_scheduled = models.DateField(auto_now_add=True)
    time_scheduled = models.TimeField(auto_now_add=True)
    pickup_lng = models.CharField(max_length=255, blank=True, default="")
    pickup_lat = models.CharField(max_length=255, blank=True, default="")
    drop_off_lat = models.CharField(max_length=255, blank=True, default="")
    drop_off_lng = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return self.schedule_type

    def get_user_name(self):
        return self.user.username

    def get_user_number(self):
        return self.user.phone_number


class ApprovedSchedules(models.Model):
    schedule = models.ForeignKey(ScheduleRide,on_delete=models.CASCADE)