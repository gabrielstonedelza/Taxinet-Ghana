from django.shortcuts import render,get_object_or_404
from .models import Notifications
from .serializers import NotificationsSerializer

from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from datetime import datetime, date, time


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).order_by('-date_created')[:50]
    serializer = NotificationsSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_unread_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(read="Not Read").order_by('date_created')
    serializer = NotificationsSerializer(notifications,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_triggered_notifications(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')[:50]
    serializer = NotificationsSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request):
    notifications = Notifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by('-date_created')
    for i in notifications:
        i.read = "Read"
        i.save()

    serializer = NotificationsSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def un_trigger_notification(request, id):
    notification = get_object_or_404(Notifications, id=id)
    serializer = NotificationsSerializer(notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_notification_detail(request,id):
    notification = get_object_or_404(Notifications, id=id)
    serializer = NotificationsSerializer(notification, many=False)
    return Response(serializer.data)