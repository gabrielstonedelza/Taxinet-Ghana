
from .models import CarsForRent, AddCarImage
from .serializers import CarsForRentSerializer, AddCarImageSerializer
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_new_car_for_rent(request):
    serializer = CarsForRentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def all_cars_for_pay_and_drive(request):
    cars_for_rent = CarsForRent.objects.all().order_by('-date_added')
    serializer = CarsForRentSerializer(cars_for_rent, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_car_for_rent(request,id):
    vehicle = get_object_or_404(CarsForRent,id=id)
    serializer = CarsForRentSerializer(vehicle, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_vehicles_for_rent_images(request, id):
    vehicle = get_object_or_404(CarsForRent,id=id)
    vehicles = AddCarImage.objects.filter(vehicle=vehicle).order_by('-date_added')
    serializer = AddCarImageSerializer(vehicles, many=True)
    return Response(serializer.data)