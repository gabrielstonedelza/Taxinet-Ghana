from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import RequestDriveAndPay
from .serializers import RequestDriveAndPaySerializer


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_drive_and_pay(request):
    serializer = RequestDriveAndPaySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_drive_and_pay_requests(request):
    my_requests = RequestDriveAndPay.objects.filter(user=request.user).order_by('-date_requested')
    serializer = RequestDriveAndPaySerializer(my_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_drive_and_pay_requests(request):
    all_requests = RequestDriveAndPay.objects.all().order_by('-date_requested')
    serializer = RequestDriveAndPaySerializer(all_requests, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_drive_and_pay(request, id):
    try:
        order = get_object_or_404(RequestDriveAndPay, id=id)
        order.delete()
    except RequestDriveAndPay.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)