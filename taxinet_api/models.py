from email.policy import default
from random import choices

from django.db import models
from django.conf import settings
from taxinet_users.models import DriverProfile, PassengerProfile, User
from django.utils import timezone

DeUser = settings.AUTH_USER_MODEL
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
SCHEDULE_TYPES = (
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Days", "Days"),
    ("Weekly", "Weekly"),
    ("Until Cancelled", "Until Cancelled"),
)

SCHEDULE_PRIORITY = (
    ("High", "High"),
    ("Low", "Low"),
)


class RequestRide(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_to_accept_ride")
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    pick_up = models.CharField(max_length=255, blank=True)
    drop_off = models.CharField(max_length=255, blank=True)
    ride_accepted = models.BooleanField(default=False)
    ride_rejected = models.BooleanField(default=False)
    passengers_lat = models.CharField(max_length=255, null=True)
    passengers_lng = models.CharField(max_length=255, null=True)
    drop_off_lat = models.CharField(max_length=255, null=True)
    drop_off_lng = models.CharField(max_length=255, null=True)
    passengers_pick_up_place_id = models.CharField(max_length=255, blank=True, default="")
    passengers_drop_off_place_id = models.CharField(max_length=255, blank=True, default="")
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    completed = models.BooleanField(default=False)
    bid_completed = models.BooleanField(default=False)
    driver_booked = models.BooleanField(default=False)
    driver_on_route = models.BooleanField(default=False)
    passenger_boarded = models.BooleanField(default=False)
    ride_distance = models.CharField(max_length=100, default="")
    ride_duration = models.CharField(max_length=100, default="")
    date_requested = models.DateField(auto_now_add=True)
    time_requested = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.driver)
        if my_driver:
            return "https://taxinetghana.xyz" + my_driver.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.passenger)
        if my_passenger:
            return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
        return ""


class AcceptedRides(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_accepting_ride")
    passengers_lat = models.CharField(max_length=255, null=True)
    passengers_lng = models.CharField(max_length=255, null=True)
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver} accepted ride {self.ride.id}"


class DriverAnnounceArrival(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_announcing_arrival")
    date_announced = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver} accepted ride {self.ride.id}"


class RejectedRides(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_rejecting_ride")
    date_rejected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver} rejected ride {self.ride.id}"


class BidRide(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE, related_name="Ride_to_accept")
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    bid = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bid)

    def get_profile_pic(self):
        deuser = User.objects.get(username=self.user.username)
        if deuser.user_type == 'Passenger':
            my_passenger = PassengerProfile.objects.get(user=self.ride.passenger)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""

        if deuser.user_type == 'Driver':
            my_driver = DriverProfile.objects.get(user=self.ride.driver)
            if my_driver:
                return "https://taxinetghana.xyz" + my_driver.profile_pic.url
            return ""


class CompletedBidOnRide(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_completing_ride")
    drivers_lat = models.CharField(max_length=255, null=True, blank=True)
    drivers_lng = models.CharField(max_length=255, null=True, blank=True)
    passengers_lat = models.CharField(max_length=255, default="")
    passengers_lng = models.CharField(max_length=255, default="")
    passengers_pickup = models.CharField(max_length=255, null=True, blank=True)
    pick_up_place_id = models.CharField(max_length=255, null=True, blank=True)
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid on ride {self.ride.id} is complete"


class CompletedRides(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.ride.id} is complete"


class RideStarted(models.Model):
    ride = models.ForeignKey(RequestRide, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Trip {self.ride.id} just started"


# working and functioning now models
class ScheduleRide(models.Model):
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_scheduling_ride")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    schedule_title = models.CharField(max_length=255, default="")
    schedule_type = models.CharField(max_length=255, default="One Time", choices=SCHEDULE_TYPES)
    schedule_priority = models.CharField(max_length=255, default="High", choices=SCHEDULE_PRIORITY)
    schedule_description = models.TextField(default="", )
    pickup_location = models.CharField(max_length=255, blank=True, )
    drop_off_location = models.CharField(max_length=255, blank=True, )
    pick_up_time = models.CharField(max_length=100, blank=True, )
    pick_up_date = models.CharField(max_length=100, blank=True, )
    completed = models.BooleanField(default=False)
    scheduled = models.BooleanField(default=False)
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    initial_payment = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_scheduled = models.DateField(auto_now_add=True)
    time_scheduled = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.schedule_title)

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.driver)
        if my_driver:
            return "https://taxinetghana.xyz" + my_driver.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.passenger)
        if my_passenger:
            return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
        return ""


class Messages(models.Model):
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE, related_name="Ride_receiving_messages")
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    message = models.TextField()
    time_sent = models.TimeField(auto_now_add=True)
    date_sent = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ride

    def get_profile_pic(self):
        de_user = User.objects.get(username=self.user.username)
        if de_user.user_type == 'Passenger':
            my_passenger = PassengerProfile.objects.get(user=self.ride.passenger)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""

        if de_user.user_type == 'Driver':
            my_driver = DriverProfile.objects.get(user=self.ride.driver)
            if my_driver:
                return "https://taxinetghana.xyz" + my_driver.profile_pic.url
            return ""


class AcceptedScheduledRides(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_accepting_scheduled_ride")
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver} accepted ride {self.scheduled_ride.id}"


class RejectedScheduledRides(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_rejecting_scheduled_ride")
    date_rejected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver} rejected ride {self.scheduled_ride.id}"


class BidScheduleRide(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE, related_name="Scheduled_Ride_to_accept")
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    bid = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.bid)

    def get_profile_pic(self):
        deUser = User.objects.get(username=self.user.username)
        if deUser.user_type == 'Passenger':
            my_passenger = PassengerProfile.objects.get(user=self.scheduled_ride.passenger)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""

        if deUser.user_type == 'Driver':
            my_driver = DriverProfile.objects.get(user=self.scheduled_ride.driver)
            if my_driver:
                return "https://taxinetghana.xyz" + my_driver.profile_pic.url
            return ""


class CompletedBidOnScheduledRide(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_completing_scheduled_ride")
    date_accepted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bid on ride {self.scheduled_ride.id} is complete"


class CompletedScheduledRides(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.scheduled_ride.id} is complete"


class ScheduledNotifications(models.Model):
    notification_id = models.CharField(max_length=100, blank=True, default="")
    notification_tag = models.CharField(max_length=255, blank=True, default="")
    notification_title = models.CharField(max_length=255, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=255, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(DeUser, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="DeUser_receiving_notification",
                                        null=True)
    passengers_pickup = models.CharField(max_length=255, null=True, blank=True)
    passengers_dropOff = models.CharField(max_length=255, null=True, blank=True)
    schedule_ride_id = models.CharField(max_length=255, blank=True)
    schedule_ride_accepted_id = models.CharField(max_length=255, blank=True)
    schedule_ride_rejected_id = models.CharField(max_length=255, blank=True)
    completed_schedule_ride_id = models.CharField(max_length=255, blank=True)
    message_id = models.CharField(max_length=255, blank=True, default='')
    complain_id = models.CharField(max_length=255, blank=True)
    reply_id = models.CharField(max_length=255, blank=True)
    review_id = models.CharField(max_length=255, blank=True)
    rating_id = models.CharField(max_length=255, blank=True)
    payment_confirmed_id = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

    def get_passengers_notification_from_pic(self):
        my_user = User.objects.get(username=self.notification_from.username)
        if my_user.user_type == "Passenger":
            my_passenger = PassengerProfile.objects.get(user=self.notification_from)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""


# working and functioning now models

class Notifications(models.Model):
    notification_id = models.CharField(max_length=100, blank=True, default="")
    notification_tag = models.CharField(max_length=255, blank=True, default="")
    notification_title = models.CharField(max_length=255, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=255, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(DeUser, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="User_receiving_notification",
                                        null=True)
    drop_off_lat = models.CharField(max_length=255, null=True, blank=True)
    drop_off_lng = models.CharField(max_length=255, null=True, blank=True)
    passengers_lat = models.CharField(max_length=255, null=True, blank=True)
    passengers_lng = models.CharField(max_length=255, null=True, blank=True)
    drivers_lat = models.CharField(max_length=255, null=True, blank=True)
    drivers_lng = models.CharField(max_length=255, null=True, blank=True)
    passengers_pickup = models.CharField(max_length=255, null=True, blank=True)
    passengers_dropOff = models.CharField(max_length=255, null=True, blank=True)
    ride_distance = models.CharField(max_length=100, default="", blank=True)
    ride_duration = models.CharField(max_length=100, default="", blank=True)
    ride_id = models.CharField(max_length=100, blank=True)
    ride_accepted_id = models.CharField(max_length=255, blank=True)
    ride_rejected_id = models.CharField(max_length=255, blank=True)
    completed_ride_id = models.CharField(max_length=255, blank=True)
    schedule_ride_id = models.CharField(max_length=255, blank=True)
    schedule_accepted_id = models.CharField(max_length=255, blank=True)
    pick_up_place_id = models.CharField(max_length=255, blank=True, default='')
    drop_off_place_id = models.CharField(max_length=255, blank=True, default='')
    message_id = models.CharField(max_length=255, blank=True, default='')
    schedule_rejected_id = models.CharField(max_length=255, blank=True)
    complain_id = models.CharField(max_length=255, blank=True)
    reply_id = models.CharField(max_length=255, blank=True)
    review_id = models.CharField(max_length=255, blank=True)
    rating_id = models.CharField(max_length=255, blank=True)
    payment_confirmed_id = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

    def get_passengers_notification_from_pic(self):
        my_user = User.objects.get(username=self.notification_from.username)
        if my_user.user_type == "Passenger":
            my_passenger = PassengerProfile.objects.get(user=self.notification_from)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""


class Complains(models.Model):
    complainant = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_making_complain")
    offender = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    complain = models.TextField(blank=True)
    read = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complainant.username} just posted a complain"

    # def get_complainant_profile_pic(self):
    #     my_driver = DriverProfile.objects.get(user=self.complainant)
    #     if my_driver:
    #         return "https://taxinetghana.xyz" + my_driver.profile_pic.url
    #     return ""
    #
    # def get_offender_profile_pic(self):
    #     my_passenger = PassengerProfile.objects.get(user=self.offender)
    #     if my_passenger:
    #         return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
    #     return ""


class DriverReviews(models.Model):
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_giving_review")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    reviews = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reviews

    # def get_passenger_profile_pic(self):
    #     my_driver = DriverProfile.objects.get(user=self.passenger)
    #     if my_driver:
    #         return "https://taxinetghana.xyz" + my_driver.profile_pic.url
    #     return ""
    #
    # def get_driver_profile_pic(self):
    #     my_passenger = PassengerProfile.objects.get(user=self.driver)
    #     if my_passenger:
    #         return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
    #     return ""


class Sos(models.Model):
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} sent an sos"


class DriversPoints(models.Model):
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_being_rated")
    points = models.IntegerField(default=0)
    date_rated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.username} gave {self.points} points to driver '{self.driver.username}'"

    # def get_passenger_profile_pic(self):
    #     my_driver = PassengerProfile.objects.get(user=self.passenger)
    #     if my_driver:
    #         return "https://taxinetghana.xyz" + my_driver.profile_pic.url
    #     return ""
    #
    # def get_driver_profile_pic(self):
    #     my_passenger = DriverProfile.objects.get(user=self.driver)
    #     if my_passenger:
    #         return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
    #     return ""


class ConfirmDriverPayment(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    payment_confirmed = models.BooleanField(default=False)
    bank_payment_reference = models.CharField(max_length=100)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_confirmed = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.payment_confirmed == "Not Confirmed":
            return f"{self.driver.username}'s previous payment pending confirmation"
        else:
            return f"{self.driver.username}'s previous payment is confirmed"

    def get_driver_profile_pic(self):
        my_passenger = DriverProfile.objects.get(user=self.driver)
        if my_passenger:
            return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
        return ""


class DriversLocation(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    place_id = models.CharField(max_length=100, blank=True)
    location_name = models.CharField(max_length=100, default="")
    drivers_lat = models.CharField(max_length=255, null=True, blank=True)
    drivers_lng = models.CharField(max_length=255, null=True, blank=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username}'s location is updated"

    def get_drivers_pic(self):
        drivers_profile = DriverProfile.objects.get(user=self.driver)
        if drivers_profile:
            return "https://taxinetghana.xyz" + drivers_profile.profile_pic.url
        return ""

    def get_drivers_name(self):
        drivers_profile = DriverProfile.objects.get(user=self.driver)
        if drivers_profile:
            return drivers_profile.name_on_ghana_card
        return ""

    def drivers_plate(self):
        drivers_profile = DriverProfile.objects.get(user=self.driver)
        if drivers_profile:
            return drivers_profile.license_plate
        return ""

    def drivers_car_model(self):
        drivers_profile = DriverProfile.objects.get(user=self.driver)
        if drivers_profile:
            return drivers_profile.car_model
        return ""

    def drivers_car_name(self):
        drivers_profile = DriverProfile.objects.get(user=self.driver)
        if drivers_profile:
            return drivers_profile.car_name
        return ""

    def drivers_taxinet_number(self):
        drivers_profile = DriverProfile.objects.get(user=self.driver)
        if drivers_profile:
            return drivers_profile.taxinet_number
        return ""


class SearchedDestinations(models.Model):
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    searched_destination = models.CharField(max_length=255)
    place_id = models.CharField(max_length=255, default="")
    drop_off_lat = models.CharField(max_length=255, null=True)
    drop_off_lng = models.CharField(max_length=255, null=True)
    date_searched = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.searched_destination
