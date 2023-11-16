from rest_framework import serializers
from .models import Booking,AddToBooked

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','user','airline','departure_airport','arrival_airport','flight_type','departure_date','departure_time','returning_date','returning_time','flight_booked','date_booked','get_username','get_user_phone']
        read_only_fields = ['user']


class AddToBookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToBooked
        fields = ['id','user','booking','date_added','get_airline','get_departure_airport','get_arrival_airport','get_flight_type','get_departure_date','get_departure_time','get_returning_date','get_returning_time','flight_booked']
        read_only_fields = ['booking']