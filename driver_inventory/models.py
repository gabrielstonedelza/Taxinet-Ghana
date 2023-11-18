from django.db import models
from users.models import User

INVENTORY_OPTIONS = (
    ("Select Option", "Select Option"),
    ("okay", "okay"),
    ("no", "no")
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

class DriverVehicleInventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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

    def __str__(self):
        return f"{self.user.username} has check car today"

    def get_user_name(self):
        return self.user.username

