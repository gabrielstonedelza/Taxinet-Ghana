from django.shortcuts import render, get_object_or_404
from .models import User, DriverProfile, PassengerProfile, AddToVerified, AddCardsUploaded, InvestorsProfile, \
    PromoterProfile
from .serializers import (UsersSerializer, DriverProfileSerializer, PassengerProfileSerializer, AddToVerifiedSerializer, \
                          AddCardsUploadedSerializer, AdminPassengerProfileSerializer, InvestorsProfileSerializer,
                          PromoterProfileSerializer)
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import filters


def taxinet_home(request):
    return render(request, "taxinet_users/taxinet_home.html")


class AllPassengersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(user_type="Passenger")
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)


class AllPassengersProfileView(generics.ListCreateAPIView):
    queryset = PassengerProfile.objects.all().order_by("-date_created")
    serializer_class = PassengerProfileSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PassengerProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class AllDriversProfileView(generics.ListCreateAPIView):
    queryset = DriverProfile.objects.all().order_by("-date_created")
    serializer_class = DriverProfileSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = DriverProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class AllUsers(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_user(request):
    users = User.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_passengers(request):
    passengers = User.objects.filter(user_type="Passenger")
    serializer = UsersSerializer(passengers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_drivers(request):
    drivers = User.objects.filter(user_type="Driver")
    serializer = UsersSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_investors(request):
    drivers = User.objects.filter(user_type="Investor")
    serializer = UsersSerializer(drivers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user(request):
    user = User.objects.filter(username=request.user.username)
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def driver_profile(request):
    my_profile = DriverProfile.objects.filter(user=request.user)
    serializer = DriverProfileSerializer(my_profile, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_driver_profile(request):
    my_profile = DriverProfile.objects.get(user=request.user)
    serializer = DriverProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def passenger_profile(request):
    my_profile = PassengerProfile.objects.filter(user=request.user)
    serializer = PassengerProfileSerializer(my_profile, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_passenger_profile(request):
    my_profile = PassengerProfile.objects.get(user=request.user)
    serializer = PassengerProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def admin_update_passenger_profile(request, id):
    my_profile = get_object_or_404(PassengerProfile, id=id)
    serializer = AdminPassengerProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_username(request):
    user = User.objects.get(username=request.user.username)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_passenger_profile(request, id):
    passenger = get_object_or_404(PassengerProfile, id=id)
    serializer = PassengerProfileSerializer(passenger, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_drivers_profile(request, id):
    driver = get_object_or_404(DriverProfile, id=id)
    serializer = DriverProfileSerializer(driver, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_drivers_profile_by_unique_code(request, unique_code):
    driver = get_object_or_404(DriverProfile, unique_code=unique_code)
    serializer = DriverProfileSerializer(driver, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_passengers_profile_by_unique_code(request, unique_code):
    passenger = get_object_or_404(PassengerProfile, unique_code=unique_code)
    serializer = PassengerProfileSerializer(passenger, many=False)
    return Response(serializer.data)


# user details
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_passenger_details(request, id):
    passenger = User.objects.filter(id=id)
    serializer = UsersSerializer(passenger, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_details(request, id):
    driver_details = User.objects.filter(id=id)
    serializer = UsersSerializer(driver_details, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_verified_profile(request):
    serializer = AddToVerifiedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_uploaded_cards(request):
    serializer = AddCardsUploadedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# search functioning
class GetAllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'full_name', 'phone_number']


class AllInvestorsProfileView(generics.ListCreateAPIView):
    queryset = InvestorsProfile.objects.all()
    serializer_class = InvestorsProfileSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = InvestorsProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class AllPromotersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(user_type="Promoter")
    serializer_class = UsersSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UsersSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_passengers(request, username):
    passengers = PassengerProfile.objects.filter(promoter=username)
    serializer = PassengerProfileSerializer(passengers, many=True)
    return Response(serializer.data)


class AllPromotersProfileView(generics.ListCreateAPIView):
    queryset = PromoterProfile.objects.all().order_by("-date_created")
    serializer_class = PromoterProfileSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PromoterProfileSerializer(queryset, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def promoter_profile(request):
    my_profile = PromoterProfile.objects.filter(user=request.user)
    serializer = PromoterProfileSerializer(my_profile, many=True)
    return Response(serializer.data)
