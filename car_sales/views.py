from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Vehicle, AddCarImage,BuyVehicle
from .serializers import VehicleSerializer, AddCarImageSerializer, BuyVehicleSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_vehicle(request):
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_vehicle_image(request):
    serializer = AddCarImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_vehicles_images(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)
    vehicles = AddCarImage.objects.filter(vehicle=vehicle).order_by('-date_added')
    serializer = AddCarImageSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_vehicle(request,id):
    vehicle = get_object_or_404(Vehicle,id=id)
    serializer = VehicleSerializer(vehicle, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_vehicles_for_sale(request):
    vehicles = Vehicle.objects.filter(purpose="For Sale").order_by('-date_added')
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_purchase_requests(request):
    purchases = BuyVehicle.objects.filter(user=request.user).order_by('-date_requested')
    serializer = BuyVehicleSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_purchase_requests(request):
    purchases = BuyVehicle.objects.all().order_by('-date_requested')
    serializer = BuyVehicleSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_purchase(request, id):
    try:
        order = get_object_or_404(BuyVehicle, id=id)
        order.delete()
    except BuyVehicle.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_vehicle(request, id):
    try:
        order = get_object_or_404(Vehicle, id=id)
        order.delete()
    except Vehicle.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_vehicles_for_rent(request):
    vehicles = Vehicle.objects.filter(purpose="For Pay And Drive").order_by('-date_added')
    serializer = VehicleSerializer(vehicles, many=True)
    return Response(serializer.data)
