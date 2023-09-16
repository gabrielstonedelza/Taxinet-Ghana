from datetime import datetime

from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from taxinet_users.models import Profile,  User
from taxinet_users.serializers import  ProfileSerializer
from .models import (Complains, ScheduledNotifications, ScheduleRide,  ContactUs,CancelScheduledRide,
                     Wallets,RentACar,RegisterCarForRent,RegisteredCarImages,
                     RegisterVehicle)
from .serializers import (ComplainsSerializer, ContactUsSerializer,RegisterCarForRentSerializer,
                           ScheduleRideSerializer,RentACarSerializer,
                          ScheduledNotificationSerializer,RegisteredCarImagesSerializer,
                          CancelledScheduledRideSerializer,
                          AdminScheduleRideSerializer, WalletsSerializer)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_image_to_registered_car(request):
    serializer = RegisteredCarImagesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_registered_images(request,id):
    car = get_object_or_404(RegisterCarForRent,id=id)
    images = RegisteredCarImages.objects.filter(registered_car=car).order_by('-date_added')
    serializer = RegisteredCarImagesSerializer(images, many=True)
    return Response(serializer.data)


# register vehicle for rental
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_car_for_rent(request):
    serializer = RegisterCarForRentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_registered_vehicles(request):
    vehicles = RegisterCarForRent.objects.all().order_by('-date_added')
    serializer = RegisterCarForRentSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_vehicle(request, id):
    vehicle = get_object_or_404(RegisterVehicle, id=id)
    serializer = RegisterCarForRentSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_vehicle_detail(request, id):
    vehicle = get_object_or_404(RegisterCarForRent, id=id)
    serializer = RegisterCarForRentSerializer(vehicle, many=False)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_vehicle(request, pk):
    try:
        car = get_object_or_404(RegisterCarForRent, pk=pk)
        car.delete()
    except RegisterCarForRent.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)

# register vehicle for rental

# rent a car
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def rent_car(request):
    serializer = RentACarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_rented_car_details(request):
    vehicles = RentACar.objects.filter(passenger=request.user).order_by('-date_booked')
    serializer = RentACarSerializer(vehicles, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_my_rented_car_status(request, id):
    vehicle = get_object_or_404(RentACar, id=id)
    serializer = RentACarSerializer(vehicle, data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_my_rented_request(request, pk):
    try:
        ride = get_object_or_404(ScheduleRide, pk=pk)
        ride.delete()
    except ScheduleRide.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)
# rent a car
# notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by(
        '-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by(
        '-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_triggered_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by('-date_created')[:50]
    for i in notifications:
        i.read = "Read"
        i.save()

    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def notification_detail(request, id):
    notification = get_object_or_404(ScheduledNotifications, id=id)
    serializer = ScheduledNotificationSerializer(notification, many=False)
    return Response(serializer.data)

# ride requests
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_ride_detail(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    if ride:
        ride.read = "Read"
        ride.save()
    serializer = ScheduleRideSerializer(ride, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def admin_update_requested_ride(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    serializer = AdminScheduleRideSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_cancelled_schedules(request):
    cancelled = ScheduleRide.objects.filter(status="Cancelled").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(cancelled, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_to_contact(request):
    serializer = ContactUsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_contact_us_messages(request):
    messages = ContactUs.objects.all().order_by('-date_sent')
    serializer = ContactUsSerializer(messages, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def cancel_schedule(request):
    serializer = CancelledScheduledRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user, )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_my_ride_requests(request):
    all_ride_requests = ScheduleRide.objects.filter(passenger=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def ride_detail(request, id):
    ride = get_object_or_404(ScheduleRide, id=id)
    serializer = ScheduleRideSerializer(ride, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def request_ride(request):
    serializer = ScheduleRideSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_requested_ride(request, ride_id):
    ride = get_object_or_404(ScheduleRide, id=ride_id)
    serializer = ScheduleRideSerializer(ride, data=request.data)
    if serializer.is_valid():
        serializer.save(passenger=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def delete_requested_ride(request, ride_id):
    try:
        ride = get_object_or_404(ScheduleRide, id=ride_id)
        ride.delete()
    except ScheduleRide.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)


# Complains
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_complain(request):
    serializer = ComplainsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(complainant=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_complains(request):
    complains = Complains.objects.all().order_by('-date_posted')
    serializer = ComplainsSerializer(complains, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def user_complains(request):
    u_complains = Complains.objects.filter(complainant=request.user).order_by('-date_posted')
    serializer = ComplainsSerializer(u_complains, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_detailed_complain(request, complain_id):
    complain = get_object_or_404(Complains, id=complain_id)
    serializer = ComplainsSerializer(complain, many=False)
    return Response(serializer.data)


# new wallet system
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def admin_load_users_wallet(request):
    serializer = WalletsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_users_wallet(request):
    wallets = Wallets.objects.exclude(user=1).order_by('-date_loaded')
    serializer = WalletsSerializer(wallets, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_user_wallet_detail(request, id):
    user = User.objects.get(id=id)
    wallet = Wallets.objects.filter(user=user)
    serializer = WalletsSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def admin_update_wallet(request, id):
    wallet = get_object_or_404(Wallets, id=id)
    serializer = WalletsSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_wallet(request):
    wallet = Wallets.objects.filter(user=request.user).order_by('-date_loaded')
    serializer = WalletsSerializer(wallet, many=True)
    return Response(serializer.data)

# searches
class SearchWallet(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Wallets.objects.all()
    serializer_class = WalletsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']


class SearchScheduleRequest(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = ScheduleRide.objects.all()
    serializer_class = ScheduleRideSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['passenger', 'schedule_type']


# new updates
@api_view(['GET', 'DELETE'])
@permission_classes([permissions.AllowAny])
def user_delete(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
    except User.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_passengers_requests(request, passenger):
    requests = ScheduleRide.objects.filter(passenger=passenger).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(requests, many=True)
    return Response(serializer.data)

