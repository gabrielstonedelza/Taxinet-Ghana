from django.db import models
from users.models import User

AIRLINES = (
    ("Africa World Airlines","Africa World Airlines"),
    ("PassionAir","PassionAir"),
    ("Hour","Hour"),
)

AIRPORTS = (
    ("Kumasi Airport (KSI)","Kumasi Airport (KSI)"),
    ("Accra (ACC)","Kumasi Airport (KSI)Accra (ACC)"),
)

FLIGHT_TYPE = (
    ("Round Trip","Round Trip"),
    ("One Way","One Way"),
)


class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    airline = models.CharField(max_length=100, choices=AIRLINES,default="PassionAir")
    departure_airport = models.CharField(max_length=100, choices=AIRPORTS,default="Kumasi Airport (KSI)")
    arrival_airport = models.CharField(max_length=100, choices=AIRPORTS,default="Kumasi Airport (KSI)")
    flight_type = models.CharField(max_length=100, choices=FLIGHT_TYPE,default="Round Trip")
    departure_date = models.CharField(max_length=20)
    departure_time = models.CharField(max_length=20)
    returning_date = models.CharField(max_length=20,blank=True)
    returning_time = models.CharField(max_length=20,blank=True)
    flight_booked = models.BooleanField(default=False)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

