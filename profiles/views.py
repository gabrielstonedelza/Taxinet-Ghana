
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import User, Profile
from .serializers import  ProfileSerializer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_profile(request):
    profile = Profile.objects.fiilter(user=request.user)
    serializer = ProfileSerializer(profile,many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
    my_profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

