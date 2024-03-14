from rest_framework import serializers
from .models import RequestDriveAndPay, AddToApprovedDriveAndPay,LockCarForTheDay, PayExtraForDriveAndPay, PayDailyForPayAndDrive


class PayDailyForPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayDailyForPayAndDrive
        fields = ['id','approved_drive','user','amount','date_paid','month_paid','year_paid']
        read_only_fields = ['user']
class PayExtraForDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PayExtraForDriveAndPay
        fields = ['id','approved_drive','user','amount','date_paid']
        read_only_fields = ['user']

class LockCarForTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = LockCarForTheDay
        fields = ['id','user','points','date_added','get_username']
        read_only_fields = ['user']

class RequestDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDriveAndPay
        fields = ['id','user','car','period','pick_up_date','drop_off_date','period_total_price','date_requested','get_username','request_approved','get_user_phone','get_car_pic','get_car_name']
        read_only_fields = ['user','car']



class AddToApprovedDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToApprovedDriveAndPay
        fields = ['id','user','drive_and_pay','assigned_driver','date_approved','get_car_name','get_drive_type','get_pick_up_date','get_drop_off_date','get_payment_period','get_total_price','get_date_requested','get_drive_type','user_tracker_sim','get_period']
        read_only_fields = ['drive_and_pay']