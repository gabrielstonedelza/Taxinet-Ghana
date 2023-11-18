from django.contrib import admin

from .models import RequestDriveAndPay,AddToApprovedDriveAndPay

class AdminDriveAndPay(admin.ModelAdmin):
    list_display =  ['id','user','car','drive_type','period','pick_up_date','drop_off_date','period_total_price','request_approved','date_requested']

    class Meta:
        model = RequestDriveAndPay

class AdminAddToApprovedDriveAndPay(admin.ModelAdmin):
    list_display = ['id','user','drive_and_pay','assigned_driver','related_name','date_approved']

    class Meta:
        model = AddToApprovedDriveAndPay


admin.site.register(RequestDriveAndPay,AdminDriveAndPay)
admin.site.register(AddToApprovedDriveAndPay,AdminAddToApprovedDriveAndPay)
