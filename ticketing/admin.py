from django.contrib import admin

from .models import Booking,AddToBooked

class AdminBooking(admin.ModelAdmin):
    list_display = ['id','user','airline','departure_airport','arrival_airport','flight_type','departure_date','departure_time','returning_date','returning_time','flight_booked','date_booked']

    class Meta:
        model = Booking


class AdminAddToBooked(admin.ModelAdmin):
    list_display = ['id','booking','user','flight_booked','date_added']
    class Meta:
        model = AddToBooked

admin.site.register(Booking,AdminBooking)
admin.site.register(AddToBooked,AdminAddToBooked)
