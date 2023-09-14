from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import filters
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UsersSerializer, ProfileSerializer


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
    queryset = Profile.objects.all().order_by("-date_created")
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
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
@permission_classes([permissions.IsAuthenticated])
def get_user(request):
    user = User.objects.filter(username=request.user.username)
    serializer = UsersSerializer(user, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def passenger_profile(request):
    my_profile = Profile.objects.filter(user=request.user)
    serializer = ProfileSerializer(my_profile, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_passenger_profile(request):
    my_profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
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
    passenger = get_object_or_404(Profile, id=id)
    serializer = ProfileSerializer(passenger, many=False)
    return Response(serializer.data)


# user details
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_passenger_details(request, id):
    passenger = User.objects.filter(id=id)
    serializer = UsersSerializer(passenger, many=True)
    return Response(serializer.data)

# search functioning
class GetAllUsers(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'full_name', 'phone_number']
# blocked users
@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def update_blocked(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_blocked_users(request):
    users = User.objects.filter(user_blocked=True)
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

