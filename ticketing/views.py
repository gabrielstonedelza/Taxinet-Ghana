from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def book_flight(request):
    serializer = BookingSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_flights(request):
    flights = Booking.objects.filter(user=request.user).order_by('-date_booked')
    serializer = BookingSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_flights(request):
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