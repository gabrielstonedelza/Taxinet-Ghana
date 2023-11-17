from rest_framework import serializers
from .models import Vehicle, AddCarImage,BuyVehicle, AddToApprovedVehiclePurchases

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id','purpose','name','price','location','milage','engine_type','interior_color','exterior_color','vin','car_id','picture','transmission','fog_light','push_start','reverse_camera','sun_roof','date_added','get_car_pic']


class AddCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCarImage
        fields = ['id','vehicle','image','date_added','get_car_pic']


class BuyVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyVehicle
        fields = ['id','user','vehicle','date_requested','request_approved','get_car_name','get_car_pic']
        read_only_fields = ['user','vehicle']

class AddToApprovedVehiclePurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToApprovedVehiclePurchases
        fields = ['id','user','vehicle','date_approved']