from django.contrib import admin

# Register your models here.
from .models import RequestDelivery


class AdminDeliver(admin.ModelAdmin):
    list_display = ['id','delivery_truck','pick_up_date','delivery_date','request_approved','date_requested']
    class Meta:
        model = RequestDelivery

admin.site.register(RequestDelivery,AdminDeliver)