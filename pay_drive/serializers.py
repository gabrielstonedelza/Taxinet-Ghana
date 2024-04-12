from rest_framework import serializers
from .models import RequestPayAndDrive, AddToApprovedPayAndDrive, PayDailyPayAndDrive,PayExtraDriveAndPay

class PayExtraDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PayExtraDriveAndPay
        fields = ['id','approved_drive','user','amount','date_paid']
        read_only_fields = ['user']
class PayDailyPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayDailyPayAndDrive
        fields = ['id','approved_drive','user','amount','date_paid']
        read_only_fields = ['user']

class RequestPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestPayAndDrive
        fields = ['id','user','car','pick_up_date','drop_off_date','period_total_price','request_approved','date_requested','get_username','get_car_pic','get_car_name','get_user_phone','referral']
        read_only_fields = ['user','car']


class AddToApprovedPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToApprovedPayAndDrive
        fields = ['id','user','pay_and_drive','assigned_driver','date_approved','get_car_name','get_driver_type','get_pick_up_date','get_total_price','get_date_requested','get_car_pic','get_drop_off_date','expired','dropped_off','get_referral','get_phone_number']
        read_only_fields = ['pay_and_drive','user']