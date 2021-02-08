from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from userSystem.models import User
from userSystem.serializers import UserCreateSerializer, UserLoginSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return Response({"message": "request error"}, status=status.HTTP_409_CONFLICT)

    if User.objects.filter(email=serializer.validated_data['email']).first() is None:
        serializer.save()
        return Response({"message": "success"}, status=status.HTTP_201_CREATED)
    return Response({"message": "duplicate email"}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({'message': 'fail'}, status=status.HTTP_200_OK)

        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)
