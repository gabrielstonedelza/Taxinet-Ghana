from rest_framework import serializers
from .models import Vehicle, AddCarImage,BuyVehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class AddCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCarImage
        fields = "__all__"


class BuyVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyVehicle
        fields = ['id','user','vehicle','date_requested']
        read_only_fields = ['user']