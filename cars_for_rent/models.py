from django.db import models

CAR_TRANSMISSIONS = (
    ("Automatic", "Automatic"),
    ("Manual", "Manual"),
)

DRIVE_TYPE = (
    ("Self Drive", "Self Drive"),
    ("With a Driver", "With a Driver"),
)

class CarsForRent(models.Model):
    name = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=10)
    seater = models.IntegerField(default=5)
    car_model = models.CharField(max_length=100,default="")
    transmission = models.CharField(max_length=100,default="Automatic")
    drive_type = models.CharField(max_length=50,default="With a Driver", choices=DRIVE_TYPE)
    color = models.CharField(max_length=100,default="Black")
    picture = models.ImageField(upload_to="Cars_for_rent")
    outside_ksi = models.BooleanField(default=False)
    k200 = models.CharField(max_length=20,default="Ghc900")
    k300 = models.CharField(max_length=20,default="Ghc1000")
    k400 = models.CharField(max_length=20,default="Ghc1200")
    k500 = models.CharField(max_length=20,default="Ghc1300")
    k600 = models.CharField(max_length=20,default="Ghc1400")
    description = models.TextField(default="")
    # inside of ksi with a driver
    kk200 = models.CharField(max_length=20,default="Ghc700")
    just_ksi = models.BooleanField(default=False)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_model

    def get_car_pic(self):
        if self.picture:
            return "https://taxinetghana.xyz" + self.picture.url
        return ''

class AddCarImage(models.Model):
    vehicle = models.ForeignKey(CarsForRent,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cars_detail_pictures")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle.name

    def get_car_pic(self):
        if self.image:
            return "https://taxinetghana.xyz" + self.image.url
        return ''
