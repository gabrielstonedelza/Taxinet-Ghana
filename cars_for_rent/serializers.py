from rest_framework import serializers
from .models import CarsForRent, AddCarImage

class CarsForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsForRent
        fields = ['id','name','engine_type','seater','transmission','car_model','picture','date_added','get_car_pic','description','color']


class AddCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCarImage
        fields = ['id','vehicle','image','date_added','get_car_pic']