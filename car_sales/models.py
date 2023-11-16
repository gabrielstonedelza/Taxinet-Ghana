from django.db import models
from users.models import User


USAGE = (
    ("Foreign Used","Foreign Used"),
    ("Local Used","Local Used"),
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

FUEL_TYPE = (
    ("Petrol","Petrol"),
    ("Gasoline","Gasoline"),
)

VEHICLE_PURPOSE = (
    ("For Sale","For Sale"),
    ("For Pay And Drive","For Pay And Drive"),
)

class Vehicle(models.Model):
    purpose = models.CharField(max_length=50,choices=VEHICLE_PURPOSE, default="For Sale")
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    location = models.CharField(max_length=100)
    milage = models.IntegerField(default=0)
    engine_type = models.CharField(max_length=30)
    interior_color = models.CharField(max_length=30,choices=COLOR_CHOICES,default="Black")
    exterior_color = models.CharField(max_length=30,choices=COLOR_CHOICES,default="Black")
    vin = models.CharField(max_length=100)
    car_id = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="cars_initial_pics")
    transmission = models.CharField(max_length=30,choices=VEHICLE_TRANSMISSION,default="Automatic")
    fog_light = models.BooleanField(default=False)
    push_start = models.BooleanField(default=False)
    reverse_camera = models.BooleanField(default=False)
    sun_roof = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AddCarImage(models.Model):
    vehicle = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cars_detail_pics")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle.name


class BuyVehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle.name
