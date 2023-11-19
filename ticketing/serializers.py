from rest_framework import serializers
from .models import Booking, AvailableFlights,RequestBooking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id','user','flight','flight_booked','date_booked','get_username','get_user_phone','adults','infants','get_airline','get_depart_airport','get_arrival_airport','get_flight_type','get_depart_date','get_flight_duration','get_depart_time','get_price','get_return_date','get_return_time','get_arrival_time']
        read_only_fields = ['flight']


class AvailableFlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableFlights
        fields = ['id','airline','departure_airport','departure_time','arrival_airport','flight_type','departure_date','flight_duration','departure_time','price','returning_date','returning_time','arrival_time','date_added']

class RequestBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestBooking
        fields = ['id','user','flight','flight_booked','date_booked','get_username','get_user_phone','adults','infants','get_airline','get_depart_airport','get_arrival_airport','get_flight_type','get_depart_date','get_flight_duration','get_depart_time','get_price','get_return_date','get_return_time','get_arrival_time']
        read_only_fields = ['flight','user']