from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from taxinet_users.models import  Profile, User

DeUser = settings.AUTH_USER_MODEL

#
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

RENT_STATUS = (
    ("Booked", "Booked"),
    ("Not Booked", "Not Booked"),
    ("Completed", "Completed"),
)

RENT_VEHICLE_TYPE = (
    ("Select Rent Type","Select Rent Type"),
    ("Truck","Truck"),
    ("Luxury","Luxury"),
    ("Bus","Bus"),
)
RENT_DRIVER_TYPE =(
    ("Select Driver Type","Select Driver Type"),
    ("Self Drive","Self Drive"),
    ("With A Driver","With A Driver"),
)
CAR_TYPE = (
    ("Select Card Type","Select Card Type"),
    ("Standard","Standard"),
    ("4WD/SUV","4WD/SUV"),
    ("Van","Van"),
)
SCHEDULE_RIDE_OPTIONS = (
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Days", "Days"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
)

SCHEDULE_TYPES = (
    ("Select Schedule Type", "Select Schedule Type"),
    ("School Pick up And Drop Off", "School Pick up And Drop Off"),
    ("Office Pick up And Drop Off", "Office Pick up And Drop Off"),
    ("Airport Pick up And Drop Off", "Airport Pick up And Drop Off"),
    ("Delivery Pick up And Drop Off", "Delivery Pick up And Drop Off"),
    ("Hotel Pick up And Drop Off", "Hotel Pick up And Drop Off"),
)

SCHEDULE_PRIORITY = (
    ("Select Schedule Priority", "Select Schedule Priority"),
    ("High", "High"),
    ("Low", "Low"),
)


INVENTORY_OPTIONS = (
    ("Select Option", "Select Option"),
    ("okay", "okay"),
    ("no", "no")
)

SCHEDULE_STATUS = (
    ("Pending", "Pending"),
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
    ("Select a brand", "Select a brand"),
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

INSPECTION_DAYS = (
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

TOP_UP_OPTIONS = (
    ("Select Payment Option", "Select Payment Option"),
    ("Mobile Money", "Mobile Money"),
    ("Ecobank", "Ecobank"),
)
SCHEDULE_DURATION = (
    ("Select Schedule Duration", "Select Schedule Duration"),
    ("One Time", "One Time"),
    ("Daily", "Daily"),
    ("Weekly", "Weekly"),
    ("Monthly", "Monthly"),
    ("Days", "Days"),
)

# working and functioning now models
class ScheduleRide(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="main_admin",default=1)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_scheduling_ride")
    schedule_type = models.CharField(max_length=255, default="Airport Pick up And Drop Off", choices=SCHEDULE_TYPES)
    schedule_duration = models.CharField(max_length=255, default="One Time", choices=SCHEDULE_DURATION)
    pickup_location = models.CharField(max_length=255, blank=True, default="")
    drop_off_location = models.CharField(max_length=255, blank=True, default="")
    pick_up_time = models.CharField(max_length=100, blank=True, )
    start_date = models.CharField(max_length=100, blank=True, )
    completed = models.BooleanField(default=False)
    day1 = models.CharField(max_length=15, blank=True, default="")
    day2 = models.CharField(max_length=15, blank=True, default="")
    day3 = models.CharField(max_length=15, blank=True, default="")
    day4 = models.CharField(max_length=15, blank=True, default="")
    day5 = models.CharField(max_length=15, blank=True, default="")
    day6 = models.CharField(max_length=15, blank=True, default="")
    day7 = models.CharField(max_length=15, blank=True, default="")
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

    def get_passenger_profile_pic(self):
        my_passenger = User.objects.get(username=self.passenger.username)
        if my_passenger.user_type == "Passenger":
            my_passenger = Profile.objects.get(user=self.passenger)
            if my_passenger:
                return "https://taxinetghana.xyz" + my_passenger.profile_pic.url
            return ""

    def get_passenger_name(self):
        return self.passenger.username

    def get_passenger_number(self):
        return self.passenger.phone_number


class CancelScheduledRide(models.Model):
    ride = models.ForeignKey(ScheduleRide, on_delete=models.CASCADE)
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_cancelling_ride")
    date_cancelled = models.DateField(auto_now_add=True)
    time_cancelled = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.ride.schedule_type


class Complains(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="complains")
    complainant = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="user_making_complain")
    complain = models.TextField(blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.complainant.username} just posted a complain"


class VehicleInventory(models.Model):
    administrator = models.ForeignKey(DeUser, on_delete=models.CASCADE, default=1, related_name="inventory")
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE)
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
    inspector_name = models.CharField(max_length=50)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.passenger.username} has check car today"

    def get_drivers_name(self):
        return self.passenger.username


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
    schedule_ride_id = models.CharField(max_length=255, blank=True)
    rent_car_id = models.CharField(max_length=255, blank=True)
    rent_car_title = models.CharField(max_length=255, blank=True)
    schedule_ride_title = models.CharField(max_length=255, blank=True)
    completed_schedule_ride_id = models.CharField(max_length=255, blank=True)
    drivers_inventory_id = models.CharField(max_length=255, blank=True, default='')
    complain_id = models.CharField(max_length=255, blank=True)
    reply_id = models.CharField(max_length=255, blank=True)
    review_id = models.CharField(max_length=255, blank=True)
    rating_id = models.CharField(max_length=255, blank=True)
    payment_confirmed_id = models.CharField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title


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
        if user.user_type == "Passenger":
            de_passenger = Profile.objects.get(user=self.user)
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
        if user.user_type == "Passenger":
            de_passenger = Profile.objects.get(user=self.user)
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


# for renting a car

class RegisterCarForRent(models.Model):
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100,choices=CAR_TYPE,default="Standard")
    number_of_passengers = models.IntegerField(default=5)
    transmission = models.CharField(max_length=100,choices=VEHICLE_TRANSMISSION,default="Automatic")
    air_condition = models.BooleanField(default=False)
    car_color = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="registered_cars",default="taxinet_cab.png")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_car_picture(self):
        if self.picture:
            return "https://taxinetghana.xyz" + self.picture.url
        return ''

class RegisteredCarImages(models.Model):
    registered_car = models.ForeignKey(RegisterCarForRent, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="register_car_images")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date_added.name

    def get_car_picture(self):
        if self.image:
            return "https://taxinetghana.xyz" + self.image.url
        return ''

class RentACar(models.Model):
    passenger = models.ForeignKey(DeUser, on_delete=models.CASCADE, related_name="passenger_renting")
    number_of_days_renting = models.IntegerField(default=1)
    pick_up_time = models.CharField(max_length=30)
    pick_up_date = models.CharField(max_length=30)
    drop_off_time = models.CharField(max_length=30)
    drop_off_date = models.CharField(max_length=30)
    rented_car = models.ForeignKey(RegisterCarForRent, on_delete=models.CASCADE, related_name="rented_car")
    driver_type = models.CharField(max_length=255, choices=RENT_DRIVER_TYPE, default="Self Drive")
    rent_status = models.CharField(max_length=105, choices=RENT_STATUS, default="Not Booked")
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.username} has requested to rent {self.rent_vehicle_type}"

    def get_passenger_name(self):
        return self.passenger.username

    def get_passenger_full_name(self):
        return self.passenger.full_name

    def get_passenger_phone_number(self):
        return self.passenger.phone_number

    def get_rented_car_name(self):
        return self.rented_car.name

    def get_car_type(self):
        return self.rented_car.car_type

    def get_car_num_of_passenger(self):
        return self.rented_car.number_of_passengers

    def get_car_transmission(self):
        return self.rented_car.transmission

    def get_car_air_condition(self):
        return self.rented_car.air_condition

    def get_car_color(self):
        return self.rented_car.car_color

    def get_rented_car_picture(self):
        if self.rented_car.picture:
            return "https://taxinetghana.xyz" + self.rented_car.picture.url
        return ''



