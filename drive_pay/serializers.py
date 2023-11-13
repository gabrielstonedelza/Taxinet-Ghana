from rest_framework import serializers
from .models import RequestDriveAndPay

class RequestDriveAndPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDriveAndPay
        fields = ['id','user','car','period','pick_up_date','drop_off_date','period_total_price','date_requested','get_username','request_approved']
        read_only_fields = ['user']
