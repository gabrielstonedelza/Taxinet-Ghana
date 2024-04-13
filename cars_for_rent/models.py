from django.db import models

class CarsForRent(models.Model):
    name = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=10)
    seater = models.IntegerField(default=5)
    daily_payment = models.CharField(max_length=500)
    above_a_week = models.CharField(max_length=500)
    picture = models.ImageField(upload_to="Cars_for_rent")
    description = models.TextField(default="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

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
