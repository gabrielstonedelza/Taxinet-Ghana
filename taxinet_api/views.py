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
                     Wallets,RentACar,RegisterCarForRent,
                     RegisterVehicle, LoadWallet)
from .serializers import (ComplainsSerializer, ContactUsSerializer,RegisterCarForRentSerializer,
                           ScheduleRideSerializer,RentACarSerializer,
                          ScheduledNotificationSerializer,
                          CancelledScheduledRideSerializer,
                          AdminScheduleRideSerializer, WalletsSerializer)


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
    vehicles = RentACar.objects.all().order_by('-date_booked')
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

# rent a car
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=1).order_by('-date_created')[:6]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_five_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('date_scheduled')[:6]
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_all_requests_by_date(request, request_date):
    all_ride_requests = ScheduleRide.objects.filter(date_scheduled=request_date).order_by('-date_scheduled')
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
def admin_get_pending_schedules(request):
    pending = ScheduleRide.objects.filter(status="Pending").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(pending, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_reviewing_schedules(request):
    reviewing = ScheduleRide.objects.filter(status="Reviewing").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(reviewing, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_active_schedules(request):
    active = ScheduleRide.objects.filter(status="Active").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(active, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_cancelled_schedules(request):
    cancelled = ScheduleRide.objects.filter(status="Cancelled").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(cancelled, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_short_trips(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="Short Trip").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_type="Daily").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_type="Days").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Weekly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_monthly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Monthly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
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
def get_all_cancelled_ride(request):
    cancelled = CancelScheduledRide.objects.all().order_by('-date_cancelled')
    serializer = CancelledScheduledRideSerializer(cancelled, many=True)
    return Response(serializer.data)



# get all requests
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def get_all_requests(request):
    all_ride_requests = ScheduleRide.objects.all().order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(all_ride_requests, many=True)
    return Response(serializer.data)


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


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_requests_completed(request):
    passenger_requests = ScheduleRide.objects.filter(passenger=request.user).filter(completed=True).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(passenger_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_requests_completed(request):
    drivers_requests = ScheduleRide.objects.filter(driver=request.user).filter(completed=True).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(drivers_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_requests_uncompleted(request):
    passenger_requests = ScheduleRide.objects.filter(passenger=request.user).filter(completed=False).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(passenger_requests, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_requests_uncompleted(request):
    drivers_requests = ScheduleRide.objects.filter(driver=request.user).filter(completed=False).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(drivers_requests, many=True)
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
@permission_classes([permissions.IsAuthenticated])
def delete_requested_ride(request, ride_id):
    try:
        ride = get_object_or_404(ScheduleRide, id=ride_id)
        ride.delete()
    except ScheduleRide.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_one_time(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="One Time").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_type="Daily").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_type="Days").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Weekly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_by_passenger(request):
    scheduled_ride = ScheduleRide.objects.filter(passenger=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(scheduled_ride, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_scheduled_by_driver(request):
    scheduled_ride = ScheduleRide.objects.filter(driver=request.user).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(scheduled_ride, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to_passenger=request.user).order_by(
        '-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_driver_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by(
        '-date_created')
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



# passengers schedules categorized
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_active_schedules(request):
    active_schedule = ScheduleRide.objects.filter(passenger=request.user).filter(status="Active").order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(active_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drives_assigned_schedules(request):
    assigned_schedules = ScheduleRide.objects.filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(assigned_schedules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drives_assigned_and_active_schedules(request):
    assigned_schedules = ScheduleRide.objects.filter(assigned_driver=request.user).filter(status="Active").order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(assigned_schedules, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# get schedule types and driver
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_short_trip(request):
    one_time_schedule = ScheduleRide.objects.filter(schedule_type="Short Trip").filter(
        assigned_driver=request.user).filter(completed=False).order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(one_time_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_daily(request):
    daily_schedule = ScheduleRide.objects.filter(schedule_type="Daily").filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(daily_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_days(request):
    days_schedule = ScheduleRide.objects.filter(schedule_type="Days").filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(days_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_weekly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Weekly").filter(assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_driver_scheduled_for_monthly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Monthly").filter(
        assigned_driver=request.user).order_by(
        '-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# passenger notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_passenger_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by(
        '-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passenger_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by(
        '-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_passengers_triggered_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')[:50]
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def admin_get_scheduled_for_monthly(request):
    weekly_schedule = ScheduleRide.objects.filter(schedule_type="Monthly").order_by('-date_scheduled')
    serializer = ScheduleRideSerializer(weekly_schedule, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



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
def user_wallet_detail(request, id):
    wallet = get_object_or_404(Wallets, id=id)
    serializer = WalletsSerializer(wallet, many=False)
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


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def user_update_wallet(request, user):
    wallet = get_object_or_404(Wallets, user=user)
    serializer = WalletsSerializer(wallet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get wallet by user
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_wallet_by_user(request, user_id):
    wallet = get_object_or_404(Wallets, user=user_id)
    serializer = WalletsSerializer(wallet, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_wallet_by_username(request, username):
    wallet = get_object_or_404(Wallets, username=username)
    serializer = WalletsSerializer(wallet, many=False)
    return Response(serializer.data)


# searches
class SearchWallet(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Wallets.objects.all()
    serializer_class = WalletsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']


class SearchScheduleRequest(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = ScheduleRide.objects.all()
    serializer_class = ScheduleRideSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['passenger_username', 'passenger_phone', 'driver_username', 'driver_phone', 'schedule_title']


class SearchPassenger(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'phone']



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

