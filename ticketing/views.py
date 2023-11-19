from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Booking, AvailableFlights,RequestBooking
from .serializers import BookingSerializer, AvailableFlightsSerializer,RequestBookingSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_available_flight_details(request):
    serializer = AvailableFlightsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_available_flights(request):
    flights = AvailableFlights.objects.all().order_by('-date_added')
    serializer = AvailableFlightsSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_available_flights_for_passion_air(request):
    flights = AvailableFlights.objects.filter(airline="PassionAir").order_by('-date_added')
    serializer = AvailableFlightsSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_available_flights_for_awa(request):
    flights = AvailableFlights.objects.filter(airline="Africa World Airlines").order_by('-date_added')
    serializer = AvailableFlightsSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def book_flight(request,flight_id):
    flight = get_object_or_404(AvailableFlights,id=id)
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(flight=flight)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_booked_flights(request):
    flights = Booking.objects.filter(user=request.user).order_by('-date_booked')
    serializer = BookingSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_booked_flights(request):
    flights = Booking.objects.all().order_by('-date_booked')
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

# request flight
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_flight(request,flight_id):
    flight = get_object_or_404(AvailableFlights,id=flight_id)
    serializer = RequestBookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(flight=flight,user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_requested_flights(request):
    flights = RequestBooking.objects.filter(user=request.user).order_by('-date_booked')
    serializer = RequestBookingSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_requested_flights(request):
    flights = RequestBooking.objects.all().order_by('-date_booked')
    serializer = RequestBookingSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_flight(request, id):
    try:
        order = get_object_or_404(RequestBooking, id=id)
        order.delete()
    except RequestBooking.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)