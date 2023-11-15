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

class AddToBooked(models.Model):
    booking = models.ForeignKey(Booking,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_being_booked")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_airline(self):
        return self.booking.airline

    def get_departure_airport(self):
        return self.booking.departure_airport

    def get_arrival_airport(self):
        return self.booking.arrival_airport

    def get_flight_type(self):
        return self.booking.flight_type

    def get_departure_date(self):
        return self.booking.departure_date

    def get_departure_time(self):
        return self.booking.departure_time

    def get_returning_date(self):
        return self.booking.returning_date

    def get_returning_time(self):
        return self.booking.returning_time
