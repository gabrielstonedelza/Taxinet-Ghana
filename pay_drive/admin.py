from django.contrib import admin

from .models import RequestPayAndDrive, AddToApprovedPayAndDrive

class AdminRequestPayAndDrive(admin.ModelAdmin):
    list_display = ['id','user','car','drive_type','pick_up_date','payment_period','period_total_price','request_approved','date_requested']
    class Meta:
        model = RequestPayAndDrive

class AdminAddToApprovedPayAndDrive(admin.ModelAdmin):
    list_display = ['id','pay_and_drive','user','assigned_driver','date_approved']
    class Meta:
        model = AddToApprovedPayAndDrive

admin.site.register(RequestPayAndDrive,AdminRequestPayAndDrive)
admin.site.register(AddToApprovedPayAndDrive,AdminAddToApprovedPayAndDrive)
