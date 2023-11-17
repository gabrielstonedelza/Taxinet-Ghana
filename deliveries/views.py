from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import RequestDelivery
from .serializers import RequestDeliverySerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def request_delivery(request):
    serializer = RequestDeliverySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_delivery_requests(request):
    deliveries = RequestDelivery.objects.filter(user=request.user).order_by('-date_requested')
    serializer = RequestDeliverySerializer(deliveries, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_deliveries(request):
    deliveries = RequestDelivery.objects.filter(request_approved="Pending").order_by('-date_requested')
    serializer = RequestDeliverySerializer(deliveries, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_delivery(request, id):
    try:
        order = get_object_or_404(RequestDelivery, id=id)
        order.delete()
    except RequestDelivery.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)