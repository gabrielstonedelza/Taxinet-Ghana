from rest_framework import serializers
from .models import CarsForRent, AddCarImage

class CarsForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarsForRent
        fields = ['id','name','engine_type','seater','transmission','car_model','picture','date_added','get_car_pic','description','color','drive_type','outside_ksi','k200','k300','k400','k500','k600','kk200','just_ksi']

class AddCarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCarImage
        fields = ['id','vehicle','image','date_added','get_car_pic']