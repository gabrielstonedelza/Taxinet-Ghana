from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import DriverVehicleInventory
from .serializers import DriverVehicleInventorySerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_inventory(request):
    serializer = DriverVehicleInventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_inventories(request):
    inventories = DriverVehicleInventory.objects.filter(user=request.user).order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_inventories(request):
    inventories = DriverVehicleInventory.objects.all().order_by('-date_checked')
    serializer = DriverVehicleInventorySerializer(inventories, many=True)
    return Response(serializer.data)
