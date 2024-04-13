from django.contrib import admin

from .models import RequestPayAndDrive, AddToApprovedPayAndDrive, PayDailyPayAndDrive

class AdminRequestPayAndDrive(admin.ModelAdmin):
    list_display = ['id','user','car','drive_type','pick_up_date','period_total_price','request_approved','date_requested','referral','pick_up_time','pick_up_location']
    class Meta:
        model = RequestPayAndDrive

class AdminAddToApprovedPayAndDrive(admin.ModelAdmin):
    list_display = ['id','pay_and_drive','user','assigned_driver','date_approved','expired','dropped_off']
    class Meta:
        model = AddToApprovedPayAndDrive

admin.site.register(RequestPayAndDrive,AdminRequestPayAndDrive)
admin.site.register(AddToApprovedPayAndDrive,AdminAddToApprovedPayAndDrive)
admin.site.register(PayDailyPayAndDrive)