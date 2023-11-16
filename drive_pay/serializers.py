from rest_framework import serializers
from .models import RequestDriveAndPay, AddToApprovedDriveAndPay

class RequestDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDriveAndPay
        fields = ['id','user','car','period','pick_up_date','drop_off_date','period_total_price','date_requested','get_username','request_approved','get_user_phone','get_car_pic']
        read_only_fields = ['user','car']



class AddToApprovedDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToApprovedDriveAndPay
        fields = ['id','user','drive_and_pay','assigned_driver','date_approved','get_car_name','get_drive_type','get_pick_up_date','get_drop_off_date','get_payment_period','get_total_price','get_date_requested']
        read_only_fields = ['drive_and_pay']
