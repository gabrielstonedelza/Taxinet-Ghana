from email.policy import default
from random import choices

from django.db import models
from django.conf import settings
from taxinet_users.models import DriverProfile, PassengerProfile

User = settings.AUTH_USER_MODEL
# Create your models here.

NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)

DRIVER_STATUS = (
    ("Booked", "Booked"),
    ("Not Booked", "Not Booked"),
)

ACCEPT_SCHEDULE_RIDE = (
    ("Accept", "Accept"),
    ("Reject", "Reject"),
)
ACCEPT_RIDE_STATUS = (
    ("Accepted", "Accepted"),
    ("Rejected", "Rejected"),
)

SCHEDULE_RIDE_OPTIONS = (
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Days", "Days"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
)

DRIVER_PAYMENT_CONFIRMATION = (
    ("Confirmed", "Confirmed"),
    ("Not Confirmed", "Not Confirmed"),
)


class RequestRide(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_to_accept_ride")
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    pick_up = models.CharField(max_length=255)
    drop_off = models.CharField(max_length=255)
    ride_accepted = models.BooleanField(default=False)
    ride_rejected = models.BooleanField(default=False)
    price = models.FloatField(blank=True)
    completed = models.BooleanField(default=False)
    driver_status = models.CharField(max_length=20, choices=DRIVER_STATUS, default="Not Booked")
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.username} has requested a ride"

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.driver)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.passenger)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class AcceptRide(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE, related_name="Ride_to_accept")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.CharField(max_length=10, blank=True)
    price = models.FloatField(blank=True)
    accept = models.BooleanField(default=False)
    reject_ride = models.CharField(max_length=10, choices=ACCEPT_RIDE_STATUS, default="Not Accepted Yet")
    driver_approved = models.CharField(blank=True, max_length=20, default="Not Approved")
    passenger_approved = models.CharField(blank=True, max_length=20, default="Not Approved")
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} has accepted ride from {self.ride.passenger.username}"

    def save(self, *args, **kwargs):
        self.price = self.bid
        self.ride.price = self.price
        super().save(*args, **kwargs)

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.ride.driver)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.ride.passenger)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


# class BargainPrice(models.Model):
#     ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE, related_name="Ride_to_bargain")
#     passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passenger_bargaining")
#     driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_bargaining")
#     message = models.TextField(blank=True)
#     is_driver = models.CharField(max_length=10, blank=True)
#     is_passenger = models.CharField(max_length=10, blank=True)
#     date_bargained = models.DtatetimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.message


class ScheduleRide(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name="passenger_scheduling_ride")
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_pickup = models.DateField()
    time_of_pickup = models.TimeField()
    schedule_option = models.CharField(max_length=30, choices=SCHEDULE_RIDE_OPTIONS, default="One Time")
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    confirmation_status = models.CharField(max_length=20, default="Not Accepted")
    scheduled = models.BooleanField(default=False)
    price = models.FloatField(blank=True)
    date_scheduled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.confirmation_status == "Accept":
            return f"{self.driver.username} has accepted scheduled ride by {self.passenger.username}"
        else:
            return "Scheduled ride not accepted by drivers yet"

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.driver)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.passenger)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class AcceptScheduleRide(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE, related_name="Scheduled_Ride_to_accept")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid = models.CharField(max_length=10, blank=True)
    price = models.FloatField(blank=True)
    accept = models.BooleanField(default=False)
    reject_scheduled = models.CharField(max_length=10, choices=ACCEPT_RIDE_STATUS, default="Not Accepted Yet")
    driver_approved = models.CharField(blank=True, max_length=20, default="Not Approved")
    passenger_approved = models.CharField(blank=True, max_length=20, default="Not Approved")
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.scheduled_ride.passenger.username}'s ride is awaiting approval"

    def save(self, *args, **kwargs):
        self.price = self.bid
        self.scheduled_ride.price = self.price
        super().save(*args, **kwargs)

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.scheduled_ride.driver)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.scheduled_ride.passenger)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class Notifications(models.Model):
    notification_id = models.CharField(max_length=100, blank=True, default="")
    notification_tag = models.CharField(max_length=100, blank=True, default="")
    notification_title = models.CharField(max_length=200, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=100, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User_receiving_notification",
                                        null=True)
    ride_id = models.CharField(max_length=100, blank=True)
    ride_accepted_id = models.CharField(max_length=100, blank=True)
    ride_rejected_id = models.CharField(max_length=100, blank=True)
    completed_ride_id = models.CharField(max_length=100, blank=True)
    schedule_ride_id = models.CharField(max_length=100, blank=True)
    schedule_accepted_id = models.CharField(max_length=100, blank=True)
    schedule_rejected_id = models.CharField(max_length=100, blank=True)
    complain_id = models.CharField(max_length=100, blank=True)
    reply_id = models.CharField(max_length=100, blank=True)
    review_id = models.CharField(max_length=100, blank=True)
    rating_id = models.CharField(max_length=100, blank=True)
    payment_confirmed_id = models.CharField(max_length=100, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

    def get_notification_from_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.notification_from)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_notification_to_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.notification_to)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class Complains(models.Model):
    complainant = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_making_complain")
    offender = models.ForeignKey(User, on_delete=models.CASCADE)
    complain = models.TextField(blank=True)
    reply = models.TextField(blank=True)
    read = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complainant.username} just posted a complain"

    def get_complainant_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.complainant)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_offender_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.offender)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class DriverReviews(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_giving_review")
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviews

    def get_passenger_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.passenger)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_driver_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.driver)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class Sos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} sent an sos"


class RateDriver(models.Model):
    passenger = models.ForeignKey(User, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="driver_being_rated")
    rating = models.IntegerField(default=0)
    date_rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.username} gave a rating of {self.rating} to driver {self.driver.username}"

    def get_passenger_profile_pic(self):
        my_driver = PassengerProfile.objects.get(user=self.passenger)
        if my_driver:
            return "http://127.0.0.1:8000" + my_driver.profile_pic.url
        return ""

    def get_driver_profile_pic(self):
        my_passenger = DriverProfile.objects.get(user=self.driver)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""


class ConfirmDriverPayment(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_confirmed = models.CharField(max_length=50, choices=DRIVER_PAYMENT_CONFIRMATION, default="Not Confirmed")
    bank_payment_reference = models.CharField(max_length=100)
    amount = models.FloatField()
    date_confirmed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.payment_confirmed == "Not Confirmed":
            return f"{self.driver.username}'s previous payment pending confirmation"
        else:
            return f"{self.driver.username}'s previous payment is confirmed"

    def get_driver_profile_pic(self):
        my_passenger = DriverProfile.objects.get(user=self.driver)
        if my_passenger:
            return "http://127.0.0.1:8000" + my_passenger.profile_pic.url
        return ""
