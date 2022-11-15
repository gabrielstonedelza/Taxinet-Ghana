from email.policy import default
from random import choices
from sre_constants import CATEGORY

from django.shortcuts import get_object_or_404
from django.db import models
from django.conf import settings
from taxinet_users.models import DriverProfile, PassengerProfile, User, InvestorsProfile, AdministratorsProfile
from django.utils import timezone
from django.utils.text import slugify

DeUser = settings.AUTH_USER_MODEL

#


from datetime import datetime, date, time, timedelta

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
    ("Short Trip", "Short Trip"),
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
    ("Select Option", "Select Option"),
    ("okay", "okay"),
    ("no", "no")
)

SCHEDULE_STATUS = (
    ("Pending", "Pending"),
    ("Reviewing", "Reviewing"),
    ("Active", "Active"),
    ("Cancelled", "Cancelled"),
)
VEHICLE_STATUS = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
    ("Inspection", "Inspection"),
    ("In the shop", "In the shop"),
    ("Stolen", "Stolen"),
    ("In Garage", "In Garage"),
)

VEHICLE_BRANDS = (
    ("Audi", "Audi"),
    ("BMW", "BMW"),
    ("Chevrolet", "Chevrolet"),
    ("Ford", "Ford"),
    ("Fiat", "Fiat"),
    ("Honda", "Honda"),
    ("Hyundai", "Hyundai"),
    ("Infinity", "Infinity"),
    ("Jeep", "Jeep"),
    ("Kia", "Kia"),
    ("Lexus", "Lexus"),
    ("Mazda", "Mazda"),
    ("Mitsubishi", "Mitsubishi"),
    ("Nissan", "Nissan"),
    ("Opel", "Opel"),
    ("Peugeot", "Peugeot"),
    ("Renault", "Renault"),
    ("Suzuki", "Suzuki"),
    ("Toyota", "Toyota"),
    ("Volkswagen", "Volkswagen"),
)

COLOR_CHOICES = (
    ("Yellow", "Yellow"),
    ("White", "White"),
    ("Black", "Black"),
    ("Gray", "Gray"),
    ("Red", "Red"),
    ("Dark Blue", "Dark Blue"),
    ("Light Blue", "Light Blue"),
    ("Brown", "Brown"),
    ("Green", "Green"),
    ("Pink", "Pink"),
    ("Orange", "Orange"),
    ("Purple", "Purple"),
    ("Beige", "Beige"),
)

VEHICLE_TRANSMISSION = (
    ("Mechanical", "Mechanical"),
    ("Automatic", "Automatic"),
    ("Robotized", "Robotized"),
    ("Variator", "Variator"),
)

BOOSTERS = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)

SAFETY_SEATS = (
    ("0", "0"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)
FLEET_CAR = (
    ("Unselected", "Unselected"),
    ("Yes", "Yes"),
    ("No", "No"),
)

VEHICLE_CATEGORY = (
    ("Comfort", "Comfort"),
    ("Courier", "Courier"),
    ("Economy", "Economy"),
    ("Delivery", "Delivery"),
)

TOYOTA_BRANDS = (
    ("Avalon", "Avalon"),
    ("BELTA", "BELTA"),
    ("CAMRY", "CAMRY"),
    ("CENTURY", "CENTURY"),
    ("ALLION", "ALLION"),
    ("LEVIN GT", "LEVIN GT"),
    ("CROWN", "CROWN"),
    ("ETIOS", "ETIOS"),
    ("MIRAI", "MIRAI"),
    ("PRIUS", "PRIUS"),
    ("AGYA", "AGYA"),
    ("AQUA", "AQUA"),
    ("COROLLA", "COROLLA"),
    ("ETIOS", "ETIOS"),
    ("GLANZA", "GLANZA"),
    ("PASSO", "PASSO"),
    ("YARIS", "YARIS"),
    ("4RUNNER", "4RUNNER"),
    ("VENZA", "VENZA"),
    ("HIGHLANDER", "HIGHLANDER"),
    ("LAND CRUISER", "LAND CRUISER"),
    ("RAV4", "RAV4"),
    ("RUSH", "RUSH"),
    ("Vitz", "Vitz"),
)

PAYMENT_METHODS = (
    ("Select payment method", "Select payment method"),
    ("Wallet", "Wallet"),
    ("Cash", "Cash"),
)

REQUEST_STATUS = (
    ("Approved", "Approved"),
    ("Pending", "Pending")
)


# working and functioning now models
class ScheduleRide(models.Model):
    assigned_driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="driver_to_be_assigned_schedule",
                                        default=1)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_scheduling_ride")
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1)
    schedule_type = models.CharField(max_length=255, default="Short Trip", choices=SCHEDULE_TYPES)
    ride_type = models.CharField(max_length=50, default="Taxinet Ride", choices=RIDE_TYPE)
    pickup_location = models.CharField(max_length=255, blank=True, default="")
    drop_off_location = models.CharField(max_length=255, blank=True, default="")
    pick_up_time = models.CharField(max_length=100, blank=True, )
    start_date = models.CharField(max_length=100, blank=True, )
    completed = models.BooleanField(default=False)
    days = models.CharField(max_length=200, blank=True, default="")
    status = models.CharField(max_length=50, choices=SCHEDULE_STATUS, default="Pending")
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    charge = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    slug = models.SlugField(max_length=100, default='', blank=True)
    date_scheduled = models.DateField(auto_now_add=True)
    time_scheduled = models.TimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")
    passenger_username = models.CharField(max_length=100, default="", blank=True, )
    passenger_phone = models.CharField(max_length=100, default="", blank=True)
    driver_username = models.CharField(max_length=100, default="", blank=True, )
    driver_phone = models.CharField(max_length=100, default="", blank=True)
    pickup_lng = models.CharField(max_length=255, blank=True, default="")
    pickup_lat = models.CharField(max_length=255, blank=True, default="")
    drop_off_lat = models.CharField(max_length=255, blank=True, default="")
    drop_off_lng = models.CharField(max_length=255, blank=True, default="")

    def __str__(self):
        return str(self.passenger.username)

    def save(self, *args, **kwargs):
        self.passenger_username = self.passenger.username
        self.driver_username = self.assigned_driver.username
        self.passenger_phone = self.passenger.phone_number
        self.driver_phone = self.assigned_driver.phone_number
        value = self.pk
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_administrator_profile_pic(self):
        de_admin = AdministratorsProfile.objects.get(user=self.administrator)
        if de_admin:
            return "https://taxinetghana.xyz" + de_admin.profile_pic.url
        return ""

    def get_passenger_profile_pic(self):
        my_passenger = User.objects.get(username=self.passenger.username)
        if my_passenger.user_type == "Passenger":
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

    def get_passenger_number(self):
        return self.passenger.phone_number

    def get_driver_phone_number(self):
        return self.assigned_driver.phone_number

    def get_assigned_driver_name(self):
        return self.assigned_driver.username


class AssignScheduleToDriver(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1)
    ride = models.OneToOneField(ScheduleRide, on_delete=models.CASCADE)
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


class CompletedScheduledRides(models.Model):
    scheduled_ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    date_completed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ride {self.scheduled_ride.id} for today is complete"

    def get_passenger_username(self):
        return self.scheduled_ride.passenger.username

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
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="complains")
    complainant = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_making_complain")
    offender = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="offender")
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
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="inventory")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=255, default="")
    unique_number = models.CharField(max_length=30, default="")
    vehicle_brand = models.CharField(max_length=255, default="Vitz", choices=TOYOTA_BRANDS)
    millage = models.CharField(max_length=255, default="")
    windscreen = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    side_mirror = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    registration_plate = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    tire_pressure = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    driving_mirror = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    tire_thread_depth = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    wheel_nuts = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    engine_oil = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    fuel_level = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    break_fluid = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    radiator_engine_coolant = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    power_steering_fluid = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    wiper_washer_fluid = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    seat_belts = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    steering_wheel = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    horn = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    electric_windows = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    windscreen_wipers = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    head_lights = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    trafficators = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    tail_rear_lights = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    reverse_lights = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    interior_lights = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    engine_noise = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    excessive_smoke = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    foot_break = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    hand_break = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    wheel_bearing_noise = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    warning_triangle = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    fire_extinguisher = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
    first_aid_box = models.CharField(max_length=30, choices=INVENTORY_OPTIONS, default="No")
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
    notification_to_admin = models.ForeignKey(DeUser, on_delete=models.CASCADE,
                                              related_name="admin_receiving_notification",
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

    # def get_passengers_notification_from_pic(self):
    #     my_user = User.objects.get(username=self.notification_from.username)
    #     if my_user.user_type == "Passenger":
    #         my_passenger = PassengerProfile.objects.get(user=self.notification_from)
    #         if my_passenger:
    #             return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
    #         return ""


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
    passenger = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="passenger_only_profile")
    de_passenger = models.ForeignKey(PassengerProfile, on_delete=models.CASCADE,
                                     related_name="passengerloadingwallet")
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_loaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

    def get_passengers_name(self):
        return self.passenger.username

    def get_amount(self):
        return self.amount

    def get_passenger_profile_pic(self):
        return "https://taxinetghana.xyz" + self.de_passenger.profile_pic.url


class AskToLoadWallet(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="administrator")
    title = models.CharField(max_length=200, default="Wants to load wallet")
    passenger = models.ForeignKey(PassengerProfile, on_delete=models.CASCADE)
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
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="start_trip")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_enjoying_trip")
    ride = models.CharField(max_length=255, default="", )
    date_started = models.DateField(auto_now_add=True)
    time_started = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} started trip"


class DriverEndTrip(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="end_trip")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_enjoying_trip_to_end")
    ride = models.CharField(max_length=255, default="", )
    price = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS, default="Wallet")
    time_elapsed = models.CharField(max_length=225, default="00:00:00")
    date_stopped = models.DateField(auto_now_add=True)
    time_stopped = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} ended trip"


class OtherWallet(models.Model):
    sender = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_sending_wallet")
    receiver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_receiving_wallet")
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_transferred = models.DateField(auto_now_add=True)
    time_transferred = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} sent GHS{self.amount} to {self.receiver.username}"

    def get_profile_pic(self):
        sender = User.objects.get(username=self.sender.username)

        if sender.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.sender)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""

        if sender.user_type == "Passenger":
            de_passenger = PassengerProfile.objects.get(user=self.sender)
            if de_passenger:
                return "https://taxinetghana.xyz" + de_passenger.profile_pic.url
            return ""


class DriverAlertArrival(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_being_alerted")
    date_alerted = models.DateField(auto_now_add=True)
    time_alerted = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.username} has arrived"


class DriversWallet(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1,
                                      related_name="drivers_administrator_for_wallet")
    driver = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="driver_only_profile")
    de_driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE, related_name="driverswallet", null=True)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    default_amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=70.00)
    date_loaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)

    def get_drivers_name(self):
        return self.driver.username

    def get_amount(self):
        return self.amount

    def get_drivers_profile_pic(self):
        return "https://taxinetghana.xyz" + self.de_driver.profile_pic.url

    # def driver_auto_payment(self):


class DriverAskToLoadWallet(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1,
                                      related_name="administrator_loadWallet")
    title = models.CharField(max_length=200, default="Wants to load wallet")
    driver = models.ForeignKey(DriverProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_requested = models.DateField(auto_now_add=True)
    time_requested = models.TimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def save(self, *args, **kwargs):
        self.title = f"{self.driver.user.username} wants to load wallet"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_drivers_name(self):
        return self.driver.user.username

    def get_amount(self):
        return str(self.amount)

    def get_drivers_profile_pic(self):
        return "https://taxinetghana.xyz" + self.driver.profile_pic.url


class DriverAddToUpdatedWallets(models.Model):
    wallet = models.ForeignKey(DriversWallet, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.driver.username}'s wallet was updated."


class RegisterVehicle(models.Model):
    status = models.CharField(max_length=255, choices=VEHICLE_STATUS, default="In Active")
    brand = models.CharField(max_length=255, choices=VEHICLE_BRANDS, default="Toyota")
    model = models.CharField(max_length=100, default="Yaris")
    color = models.CharField(max_length=255, choices=COLOR_CHOICES, default="White")
    year = models.CharField(max_length=20, default="2000")
    license_plate_number = models.CharField(max_length=50, blank=True)
    vin = models.CharField(max_length=50, blank=True)
    body_number = models.CharField(max_length=50, blank=True)
    registration_certificate_number = models.CharField(max_length=50, blank=True)
    taxi_license_number = models.CharField(max_length=50, blank=True)
    transmission = models.CharField(max_length=30, choices=VEHICLE_TRANSMISSION, default="Automatic")
    boosters = models.CharField(max_length=4, choices=BOOSTERS, default="0")
    child_safety_seats = models.CharField(max_length=4, choices=SAFETY_SEATS, default="0")
    # branded_wrap = models.BooleanField(default=False)
    # light_box = models.BooleanField(default=False)
    # fleet_car = models.CharField(max_length=20, choices=FLEET_CAR, default="Unselected", blank=True)
    code_name = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=50, choices=VEHICLE_CATEGORY, default="Comfort")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model

    # def get_vehicle_photo(self):
    #     if self.picture:
    #         return "https://taxinetghana.xyz" + self.picture.url
    #     return ""


class AddToPaymentToday(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="payment_admin")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    title = models.CharField(max_length=255, default="Payment Today")
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")
    date_paid = models.DateField(auto_now_add=True)
    time_paid = models.TimeField(auto_now_add=True)
    username = models.CharField(max_length=100, default="", blank=True, )
    phone = models.CharField(max_length=100, default="", blank=True)

    def __str__(self):
        return f"{self.driver.username} has made payment today"

    def save(self, *args, **kwargs):
        self.username = self.driver.username
        self.phone = self.driver.phone_number
        value = f"{self.driver.username} has made payment today"
        self.title = value
        super().save(*args, **kwargs)

    def get_driver_profile_pic(self):
        driver = User.objects.get(username=self.driver.username)
        if driver.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.driver)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""

    def get_drivers_full_name(self):
        return self.driver.full_name


# new wallets
class Wallets(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="user_only_profile")
    username = models.CharField(max_length=100, default="", blank=True, )
    phone = models.CharField(max_length=100, default="", blank=True)
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_loaded = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.username = self.user.username
        self.phone = self.user.phone_number
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} wallet is loaded with GHS{self.amount}"

    def get_username(self):
        return self.user.username

    def get_full_name(self):
        return self.user.full_name

    def get_profile_pic(self):
        user = User.objects.get(username=self.user.username)
        if user.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.user)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""
        elif user.user_type == "Passenger":
            de_passenger = PassengerProfile.objects.get(user=self.user)
            if de_passenger:
                return "https://taxinetghana.xyz" + de_passenger.profile_pic.url
            return ""

    def get_user_type(self):
        return self.user.user_type


class LoadWallet(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="loadwallet_admin")
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Wants to load wallet")
    amount = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    date_requested = models.DateField(auto_now_add=True)
    time_requested = models.TimeField(auto_now_add=True)
    read = models.CharField(max_length=10, choices=READ_STATUS, default="Not Read")

    def save(self, *args, **kwargs):
        self.title = f"{self.user.username} wants to load wallet"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_profile_pic(self):
        user = User.objects.get(username=self.user.username)
        if user.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.user)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""
        elif user.user_type == "Passenger":
            de_passenger = PassengerProfile.objects.get(user=self.user)
            if de_passenger:
                return "https://taxinetghana.xyz" + de_passenger.profile_pic.url
            return ""

    def get_username(self):
        return self.user.username

    def get_full_name(self):
        return self.user.full_name

    def get_user_type(self):
        return self.user.user_type


class UpdatedWallets(models.Model):
    wallet = models.ForeignKey(Wallets, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username}'s wallet was updated."


class RideMessages(models.Model):
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    user = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_sending_message")
    message = models.TextField()
    read = models.BooleanField(default=False)
    date_sent = models.DateField(auto_now_add=True)
    time_sent = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ride.schedule_title} got a message"

    def get_profile_pic(self):
        # get driver profile
        user = User.objects.get(username=self.user.username)
        if user.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.user)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""
        elif user.user_type == "Passenger":
            de_passenger = PassengerProfile.objects.get(user=self.user)
            if de_passenger:
                return "https://taxinetghana.xyz" + de_passenger.profile_pic.url
            return ""

    def get_username(self):
        return self.user.username

    def get_user_type(self):
        return self.user.user_type


class ExpensesRequest(models.Model):
    guarantor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, null=True, related_name="driver_making_expense")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_requesting_expense_cash")
    item_name = models.CharField(max_length=200, default="")
    quantity = models.IntegerField(default=0)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    reason = models.TextField(default="")
    request_status = models.CharField(max_length=20, choices=REQUEST_STATUS, default="Pending")
    date_requested = models.DateField(auto_now_add=True)
    time_requested = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"Expense request made for {self.amount} by {self.user.username}"

    def get_username(self):
        return self.user.username

    def get_driver_username(self):
        return self.driver.username


class WorkAndPay(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    amount_to_pay = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    amount_paid = models.DecimalField(blank=True, decimal_places=2, max_digits=10, default=00.00)
    years = models.IntegerField(default=2)
    start_date = models.CharField(max_length=20, blank=True)
    end_date = models.CharField(max_length=20, blank=True)
    fully_paid = models.BooleanField(default=False)
    date_started = models.DateField(auto_now_add=True)
    time_started = models.TimeField(auto_now_add=True)

    def __srt__(self):
        return f"{self.driver.username} has been added to work and pay system"

    def get_assigned_driver_profile_pic(self):
        driver = User.objects.get(username=self.assigned_driver.username)

        if driver.user_type == "Driver":
            de_driver = DriverProfile.objects.get(user=self.assigned_driver)
            if de_driver:
                return "https://taxinetghana.xyz" + de_driver.profile_pic.url
            return ""

    def get_driver_username(self):
        return self.driver.username


# new updates
class Stocks(models.Model):
    item_name = models.CharField(max_length=200, )
    quantity = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)
    time_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name


class MonthlySalary(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    date_paid = models.DateField(auto_now_add=True)
    time_paid = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.driver.username


class PayPromoterCommission(models.Model):
    promoter = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    date_paid = models.DateField(auto_now_add=True)
    time_paid = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.promoter.username


class PrivateChatId(models.Model):
    chat_id = models.CharField(max_length=400, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.chat_id


class PrivateUserMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatter2")
    private_chat_id = models.CharField(max_length=400, blank=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    isSender = models.BooleanField(default=False)
    isReceiver = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.private_chat_id

    def get_senders_username(self):
        return self.sender.username

    def get_receivers_username(self):
        return self.receiver.username

    def save(self, *args, **kwargs):
        senders_username = self.sender.username
        receiver_username = self.receiver.username
        sender_receiver = str(senders_username) + str(receiver_username)
        receiver_sender = str(receiver_username) + str(senders_username)

        self.private_chat_id = sender_receiver

        super().save(*args, **kwargs)

    def get_sender_profile_pic(self):
        my_sender = User.objects.get(username=self.sender.username)
        if my_sender.user_type == "Passenger":
            my_passenger = PassengerProfile.objects.get(user=self.sender)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""
        if my_sender.user_type == "Driver":
            my_driver = DriverProfile.objects.get(user=self.sender)
            if my_driver:
                return "https://taxinetghana.xyz" + my_driver.profile_pic.url
            return ""


class AddToBlockList(models.Model):
    administrator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_being_blocked")
    date_blocked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username


class DriversCommission(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    date_paid = models.DateField(auto_now_add=True)
    time_paid = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.driver.username


class DriverRequestCommission(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1)
    accounts = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=2, related_name="accounts_wallet")
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="accounts_driver")
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    date_requested = models.DateField(auto_now_add=True)
    time_requested = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.driver.username


class DriverTransferCommissionToWallet(models.Model):
    driver = models.ForeignKey(DeUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    date_transferred = models.DateField(auto_now_add=True)
    time_transferred = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.driver.username
