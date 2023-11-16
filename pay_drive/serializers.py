from rest_framework import serializers
from .models import RequestPayAndDrive, AddToApprovedPayAndDrive

class RequestPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestPayAndDrive
        fields = ['id','user','car','pick_up_date','payment_period','period_total_price','request_approved','date_requested','get_username']
        read_only_fields = ['user']


class AddToApprovedPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToApprovedPayAndDrive
        fields = ['id','user','pay_and_drive','assigned_driver','date_approved','get_car_name','get_driver_type','get_pick_up_date','get_payment_period','get_total_price','get_date_requested']
        read_only_fields = ['pay_and_drive']