from django.db import models
from users.models import User


DELIVERY_VEHICLES = (
    ("Truck", "Truck"),
    ("Motor Bike", "Motor Bike"),
    ("Aboboyaa", "Aboboyaa"),
)

class RequestDelivery(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    delivery_truck = models.CharField(max_length=30,choices=DELIVERY_VEHICLES,default="Truck")
    pick_up_date = models.CharField(max_length=10)
    delivery_date = models.CharField(max_length=10)
    request_approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_user_phone(self):
        return self.user.phone_number

