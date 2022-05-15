from django.shortcuts import render, get_object_or_404
from .models import User, DriverProfile, PassengerProfile
from .serializers import UsersSerializer, DriverProfileSerializer, PassengerProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_passengers(request):
    passengers = User.objects.filter(user_type="Passenger")
    serializer = UsersSerializer(passengers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_drivers(request):
    drivers = User.objects.filter(user_type="Driver")
    serializer = UsersSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user(request):
    user = User.objects.filter(username=request.user.username)
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def driver_profile(request):
    my_profile = DriverProfile.objects.filter(user=request.user)
    serializer = DriverProfileSerializer(my_profile, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_driver_profile(request):
    my_profile = DriverProfile.objects.get(user=request.user)
    serializer = DriverProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def passenger_profile(request):
    my_profile = PassengerProfile.objects.filter(user=request.user)
    serializer = PassengerProfileSerializer(my_profile, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_passenger_profile(request):
    my_profile = PassengerProfile.objects.get(user=request.user)
    serializer = PassengerProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_username(request):
    user = User.objects.get(username=request.user.username)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
