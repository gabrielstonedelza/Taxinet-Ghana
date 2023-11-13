from django.shortcuts import render,get_object_or_404
from .models import ScheduleRide
from .serializers import ScheduleRideSerializer

from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_ride(request):
    serializer = ScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_schedules(request):
    schedules = ScheduleRide.objects.filter(user=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_schedules(request):
    schedules = ScheduleRide.objects.all().order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(schedules, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_schedule(request, id):
    try:
        order = get_object_or_404(ScheduleRide, id=id)
        order.delete()
    except ScheduleRide.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

