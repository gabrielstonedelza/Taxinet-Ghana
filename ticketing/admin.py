from django.contrib import admin

from .models import Booking,AvailableFlights,RequestBooking

class AdminBooking(admin.ModelAdmin):
    list_display = ['id','user','flight','infants','adults','flight_booked','date_booked','flight_type','returning_date','returning_time','user_phone_number','date_of_birth']

    class Meta:
        model = Booking

class AdminRequestBooking(admin.ModelAdmin):
    list_display = ['id','user','flight','infants','adults','flight_booked','date_booked']

    class Meta:
        model = RequestBooking
class AdminAvailableFlights(admin.ModelAdmin):
    list_display = ['id','airline','departure_airport','departure_time','arrival_airport','departure_date','flight_duration','departure_time','price','arrival_time','date_added']
    class Meta:
        model = AvailableFlights

admin.site.register(Booking,AdminBooking)
admin.site.register(AvailableFlights,AdminAvailableFlights)
admin.site.register(RequestBooking,AdminRequestBooking)
