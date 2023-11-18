from django.contrib import admin
from .models import ScheduleRide

class AdminSchedule(admin.ModelAdmin):
    list_display = ['id','user','schedule_type','schedule_duration','pickup_location','drop_off_location','pick_up_time','start_date','completed','status','price','charge','date_scheduled','time_scheduled']
    class Meta:
        model = ScheduleRide

admin.site.register(ScheduleRide,AdminSchedule)
