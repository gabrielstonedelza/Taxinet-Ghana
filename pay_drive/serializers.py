from rest_framework import serializers
from .models import RequestPayAndDrive

class RequestPayAndDriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestPayAndDrive
        fields = ['id','user','car','pick_up_date','payment_period','period_total_price','request_approved','date_requested','get_username']
        read_only_fields = ['user']