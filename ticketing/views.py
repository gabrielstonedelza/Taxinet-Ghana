from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Booking, AddToBooked
from .serializers import BookingSerializer, AddToBookedSerializer


@api_view(['GET','POST'])
@permission_classes([permissions.AllowAny])
def add_to_booked(request,id):
    booking = get_object_or_404(Booking,id=id)
    serializer = AddToBookedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(booking=booking)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_booked_flights(request):
    flights = AddToBooked.objects.filter(user=request.user).order_by('-date_added')
    serializer = AddToBookedSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_booked_flights(request):
    flights = AddToBooked.objects.all().order_by('-date_added')
    serializer = AddToBookedSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def book_flight(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_flight_requests(request):
    flights = Booking.objects.filter(user=request.user).filter(flight_booked="Pending").order_by('-date_booked')
    serializer = BookingSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_flight_requests(request):
    flights = Booking.objects.filter(flight_booked="Pending").order_by('-date_booked')
    serializer = BookingSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_flight(request, id):
    try:
        order = get_object_or_404(Booking, id=id)
        order.delete()
    except Booking.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)