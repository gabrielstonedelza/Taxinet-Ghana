from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','user','airline','departure_airport','arrival_airport','flight_type','departure_date','departure_time','returning_date','returning_time','flight_booked','date_booked','get_username']