from django.db import models
from users.models import User
from django.utils import timezone


AIRLINES = (
    ("Africa World Airlines","Africa World Airlines"),
    ("PassionAir","PassionAir"),
)

AIRPORTS = (
    ("Kumasi (KMS)","Kumasi (KMS)"),
    ("Accra (ACC)","Accra (ACC)"),
    ("Takoradi (TKD)","Takoradi (TKD)"),
    ("Tamale (TML)","Tamale (TML)"),
    ("Wa (WZA)","Wa (AWZA"),
    ("Sunyani (NYI)","Sunyani (NYI)"),
)

FLIGHT_TYPE = (
    ("Round Trip","Round Trip"),
    ("One Way","One Way"),
)

FLIGHT_STATUS = (
    ("Pending","Pending"),
    ("Booked","Booked"),
)

ADULTS = (
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
)

INFANTS = (
    ("0","0"),
    ("1","1"),
    ("2","2"),
    ("3","3"),
    ("4","4"),
    ("5","5"),
    ("6","6"),
    ("7","7"),
    ("8","8"),
    ("9","9"),
    ("10","10"),
)


REQUEST_STATUS = (
    ("Pending","Pending"),
    ("Booked","Booked"),
)
class AvailableFlights(models.Model):
    airline = models.CharField(max_length=100, choices=AIRLINES,default="PassionAir")
    departure_airport = models.CharField(max_length=100, choices=AIRPORTS,default="Kumasi (KSI)")
    arrival_airport = models.CharField(max_length=100, choices=AIRPORTS,default="Kumasi (KSI)")
    departure_date = models.DateField(default=timezone.now)
    arrival_date = models.DateField(default=timezone.now)
    flight_duration = models.IntegerField(default=45)
    departure_time = models.TimeField(default=timezone.now)
    arrival_time = models.TimeField(default=timezone.now)
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0.0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.airline


class Booking(models.Model):
    flight = models.ForeignKey(AvailableFlights,on_delete=models.CASCADE,related_name="chosen_flight",null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flight_booked = models.CharField(max_length=20,choices=FLIGHT_STATUS,default="Pending")
    flight_type = models.CharField(max_length=100, choices=FLIGHT_TYPE, default="Round Trip")
    user_phone_number = models.CharField(max_length=15,default="0244000000")
    date_of_birth = models.DateField(default=timezone.now)
    returning_date = models.DateField(default=timezone.now)
    returning_time = models.TimeField(default=timezone.now)
    adults = models.CharField(max_length=11, choices=ADULTS,default="1")
    infants = models.CharField(max_length=11, choices=INFANTS,default="0")
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_user_phone(self):
        return self.user.phone_number

    def get_airline(self):
        return self.flight.airline

    def get_depart_airport(self):
        return self.flight.departure_airport


    def get_arrival_airport(self):
        return self.flight.arrival_airport


    def get_depart_date(self):
        return self.flight.departure_date
    def get_arrival_date(self):
        return self.flight.arrival_date

    def get_flight_duration(self):
        return self.flight.flight_duration

    def get_depart_time(self):
        return self.flight.departure_time

    def get_price(self):
        return self.flight.price

    def get_arrival_time(self):
        return self.flight.arrival_time

class RequestBooking(models.Model):
    flight = models.ForeignKey(AvailableFlights,on_delete=models.CASCADE,related_name="chosen_flight_to_request",null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flight_booked = models.CharField(max_length=20,choices=FLIGHT_STATUS,default="Pending")
    adults = models.IntegerField(default=1)
    infants = models.IntegerField(default=0)
    date_booked = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_user_phone(self):
        return self.user.phone_number

    def get_airline(self):
        return self.flight.airline

    def get_depart_airport(self):
        return self.flight.departure_airport


    def get_arrival_airport(self):
        return self.flight.arrival_airport

    def get_depart_date(self):
        return self.flight.departure_date
    def get_arrival_date(self):
        return self.flight.arrival_date

    def get_flight_duration(self):
        return self.flight.flight_duration

    def get_depart_time(self):
        return self.flight.departure_time

    def get_price(self):
        return self.flight.price


    def get_arrival_time(self):
        return self.flight.arrival_time