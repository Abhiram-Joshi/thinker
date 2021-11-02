import jwt
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from .serializers import UserLoginSerializer, RefreshTokenSerializer
from .utilities import generate_access_token, generate_refresh_token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
# Create your views here.

class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        User = get_user_model()

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uuid = serializer.validated_data["uuid"]

        user, created = User.objects.get_or_create(
            uuid=uuid
        )

        access_token = generate_access_token(uuid)
        refresh_token = generate_refresh_token(uuid)

        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return Response(response, status=status.HTTP_200_OK)


class RefreshTokenAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        serializer = RefreshTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh_token"]

        try:
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithm="HS256")

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token expired")
        
        except jwt.InvalidSignatureError:
            raise AuthenticationFailed("Invalid token")

        access_token = generate_access_token(payload["uuid"])
        refresh_token = generate_refresh_token(payload["uuid"])

        response = {
            "access_token": access_token,
            "refresh_token": refresh_token,
        }

        return Response(response, status=status.HTTP_200_OK)