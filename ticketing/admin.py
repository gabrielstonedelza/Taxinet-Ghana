from django.contrib import admin

from .models import Booking,AvailableFlights,RequestBooking

class AdminBooking(admin.ModelAdmin):
    list_display = ['id','user','flight','infants','adults','flight_booked','date_booked']

    class Meta:
        model = Booking

class AdminRequestBooking(admin.ModelAdmin):
    list_display = ['id','user','flight','infants','adults','flight_booked','date_booked']

    class Meta:
        model = RequestBooking
class AdminAvailableFlights(admin.ModelAdmin):
    list_display = ['id','airline','departure_airport','arrival_airport','flight_type','departure_date','flight_duration','departure_time','price','returning_date','returning_time','arrival_time','date_added']
    class Meta:
        model = AvailableFlights

admin.site.register(Booking,AdminBooking)
admin.site.register(AvailableFlights,AdminAvailableFlights)
admin.site.register(RequestBooking,AdminRequestBooking)
