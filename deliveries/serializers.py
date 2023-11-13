from rest_framework import serializers
from .models import RequestDelivery


class RequestDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestDelivery
        fields = ['id','user','delivery_truck','items_delivering','pick_up_date','delivery_date','request_approved','date_requested','get_username']
        read_only_fields = ['user']