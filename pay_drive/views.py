from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import RequestPayAndDrive,AddToApprovedPayAndDrive
from .serializers import RequestPayAndDriveSerializer,AddToApprovedPayAndDriveSerializer
from django.core.mail import EmailMessage

@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_pay_and_drive_complete(request,id):
    pay_drive = get_object_or_404(RequestPayAndDrive,id=id)
    serializer = AddToApprovedPayAndDriveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(pay_and_drive=pay_drive)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_approved_pay_and_drive(request):
    my_approved = AddToApprovedPayAndDrive.objects.filter(user=request.user).order_by('-date_approved')
    serializer = AddToApprovedPayAndDriveSerializer(my_approved, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_approved_pay_and_drive(request):
    approved = AddToApprovedPayAndDrive.objects.all().order_by('-date_approved')
    serializer = AddToApprovedPayAndDriveSerializer(approved, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_pay_and_drive(request):
    serializer = RequestPayAndDriveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_pay_and_drive_requests(request):
    my_requests = RequestPayAndDrive.objects.filter(user=request.user).order_by('-date_requested')
    serializer = RequestPayAndDriveSerializer(my_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_pay_and_drive_requests(request):
    all_requests = RequestPayAndDrive.objects.all().order_by('-date_requested')
    serializer = RequestPayAndDriveSerializer(all_requests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_pay_and_drive(request, id):
    try:
        order = get_object_or_404(RequestPayAndDrive, id=id)
        order.delete()
    except RequestPayAndDrive.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)