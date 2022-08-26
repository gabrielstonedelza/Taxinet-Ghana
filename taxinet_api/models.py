from django.shortcuts import get_object_or_404
from django.db import models
from django.conf import settings
from taxinet_users.models import DriverProfile, PassengerProfile, User, InvestorsProfile, AdministratorsProfile
from django.utils import timezone
from django.utils.text import slugify

DeUser = settings.AUTH_USER_MODEL
# Create your models here.
READ_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

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
    ("Select Schedule Type", "Select Schedule Type"),
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Days", "Days"),
    ("Weekly", "Weekly"),
    ("Until Cancelled", "Until Cancelled"),
)

SCHEDULE_PRIORITY = (
    ("Select Schedule Priority", "Select Schedule Priority"),
    ("High", "High"),
    ("Low", "Low"),
)

RIDE_TYPE = (
    ("Taxinet Ride", "Taxinet Ride"),
    ("Taxinet Luxury", "Taxinet Luxury"),
)

INVENTORY_OPTIONS = (
    ("Okay", "Okay"),
    ("No", "No")
)

SCHEDULE_STATUS = (
    ("Pending", "Pending"),
    ("Reviewing", "Reviewing"),
    ("Active", "Active"),
    ("Cancelled", "Cancelled"),
)


# working and functioning now models
class ScheduleRide(models.Model):
    assigned_driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_to_be_assigned_schedule",
                                        default=1)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_scheduling_ride")
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1)
    schedule_title = models.CharField(max_length=255, default="")
    schedule_type = models.CharField(max_length=255, default="One Time", choices=SCHEDULE_TYPES)
    schedule_priority = models.CharField(max_length=255, default="High", choices=SCHEDULE_PRIORITY)
    schedule_description = models.TextField(default="", )
    ride_type = models.CharField(max_length=50, default="Taxinet Ride", choices=RIDE_TYPE)
    pickup_location = models.CharField(max_length=255, blank=True, )
    drop_off_location = models.CharField(max_length=255, blank=True, )
    pick_up_time = models.CharField(max_length=100, blank=True, )
    start_date = models.CharField(max_length=100, blank=True, )
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=SCHEDULE_STATUS, default="Pending")
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    initial_payment = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    slug = models.SlugField(max_length=100, default='', blank=True)
    date_scheduled = models.DateField(auto_now_add=True)
    time_scheduled = models.TimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        value = self.schedule_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_administrator_profile_pic(self):
        de_admin = AdministratorsProfile.objects.get(user=self.administrator)
        if de_admin:
            return "https://taxinetghana.xyz" + de_admin.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = PassengerProfile.objects.get(user=self.passenger)
        if my_passenger:
            return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
        return ""

    def get_assigned_driver_profile_pic(self):
        driver = User.objects.get(username=self.assigned_driver.username)
        if driver.user_type == "Administrator":
            de_driver = AdministratorsProfile.objects.get(user=self.assigned_driver)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""
        elif driver.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.assigned_driver)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""

    def get_passenger_name(self):
        return self.passenger.username

    def get_assigned_driver_name(self):
        return self.assigned_driver.username


class AssignScheduleToDriver(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1)
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="Driver_receiving_scheduled_ride")
    ride_accepted = models.BooleanField(default=False)
    date_assigned = models.DateField(auto_now_add=True)
    time_assigned = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ride} was assigned to {self.driver}"


class AcceptAssignedScheduled(models.Model):
    assigned_to_driver = models.ForeignKey(AssignScheduleToDriver, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    date_accepted = models.DateField(auto_now_add=True)
    time_accepted = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} accepted ride {self.assigned_to_driver.ride}"


class RejectAssignedScheduled(models.Model):
    assigned_to_driver = models.ForeignKey(AssignScheduleToDriver, on_delete=models.CASCADE)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    date_rejected = models.DateField(auto_now_add=True)
    time_rejected = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} rejected ride {self.assigned_to_driver.ride}"


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


class CompletedScheduledRidesToday(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.scheduled_ride.id} for today is complete"

    def get_passenger_username(self):
        return self.scheduled_ride.passenger.username

    def get_amount(self):
        return self.amount

    def assigned_driver(self):
        return self.scheduled_ride.assigned_driver.username


class CancelScheduledRide(models.Model):
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_cancelling_ride")
    date_cancelled = models.DateField(auto_now_add=True)
    time_cancelled = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.ride


class Complains(models.Model):
    complainant = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_making_complain")
    offender = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    complain = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def __str__(self):
        return f"{self.complainant.username} just posted a complain"


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


class DriverVehicleInventory(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    windscreen = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    side_mirror = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    registration_plate = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    tire_pressure = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    driving_mirror = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    tire_thread_depth = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    wheel_nuts = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    engine_oil = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    fuel_level = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    break_fluid = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    radiator_engine_coolant = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    power_steering_fluid = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    wiper_washer_fluid = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    seat_belts = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    steering_wheel = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    horn = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    electric_windows = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    windscreen_wipers = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    head_lights = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    trafficators = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    tail_rear_lights = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    reverse_lights = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    interior_lights = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    engine_noise = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    excessive_smoke = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    foot_break = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    hand_break = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    wheel_bearing_noise = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    warning_triangle = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    fire_extinguisher = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    first_aid_box = models.CharField(max_length=10, choices=INVENTORY_OPTIONS, default="No")
    checked_today = models.BooleanField(default=False)
    date_checked = models.DateField(auto_now_add=True)
    time_checked = models.TimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def __str__(self):
        return f"{self.driver.username} has check car today"

    def get_drivers_name(self):
        return self.driver.username

    def get_driver_profile_pic(self):
        my_driver = DriverProfile.objects.get(user=self.driver)
        if my_driver:
            return "https://taxinetghana.xyz" + my_driver.profile_pic.url
        return ""


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
    notification_to_passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE,
                                                  related_name="Passenger_receiving_notification",
                                                  null=True)
    passengers_pickup = models.CharField(max_length=255, null=True, blank=True)
    passengers_dropOff = models.CharField(max_length=255, null=True, blank=True)
    schedule_ride_slug = models.CharField(max_length=255, blank=True)
    schedule_ride_id = models.CharField(max_length=255, blank=True)
    schedule_ride_title = models.CharField(max_length=255, blank=True)
    schedule_ride_accepted_id = models.CharField(max_length=255, blank=True)
    schedule_ride_rejected_id = models.CharField(max_length=255, blank=True)
    completed_schedule_ride_id = models.CharField(max_length=255, blank=True)
    drivers_inventory_id = models.CharField(max_length=255, blank=True, default='')
    assigned_scheduled_id = models.CharField(max_length=255, blank=True, default='')
    accept_assigned_scheduled_id = models.CharField(max_length=255, blank=True, default='')
    reject_assigned_scheduled_id = models.CharField(max_length=255, blank=True, default='')
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


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def __str__(self):
        return self.name


class ContactAdmin(models.Model):
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def __str__(self):
        return self.user.username


class PassengersWallet(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1,
                                      related_name="administrator_for_wallet")
    passenger = models.OneToOneField(PassengerProfile, on_delete=models.CASCADE, related_name="passenger_only_profile")
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_loaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

    def get_passengers_name(self):
        return self.passenger.user.username

    def get_amount(self):
        return self.amount

    def get_passenger_profile_pic(self):
        return "https://taxinetghana.xyz" + self.passenger.profile_pic.url


class AskToLoadWallet(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="administrator")
    title = models.CharField(max_length=200, default="Wants to load wallet")
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_requested = models.DateField(auto_now_add=True)
    time_requested = models.TimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def save(self, *args, **kwargs):
        self.title = f"{self.passenger.user.username} wants to load wallet"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_passengers_name(self):
        return self.passenger.user.username

    def get_amount(self):
        return str(self.amount)

    def get_passenger_profile_pic(self):
        return "https://taxinetghana.xyz" + self.passenger.profile_pic.url


class AddToUpdatedWallets(models.Model):
    wallet = models.ForeignKey(PassengersWallet, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.passenger.username}'s wallet was updated."


class DriverStartTrip(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_enjoying_trip")
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE, related_name="trip_ride")
    date_started = models.DateField(auto_now_add=True)
    time_started = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} started trip"


class DriverEndTrip(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_enjoying_trip_to_end")
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE, related_name="trip_ride_end")
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_stopped = models.DateField(auto_now_add=True)
    time_stopped = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} ended trip"


class DriverAlertArrival(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_being_alerted")
    date_alerted = models.DateField(auto_now_add=True)
    time_alerted = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} has arrived"
