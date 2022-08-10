import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from utilities import get_model_fields, response_writer

from .serializers import RefreshTokenSerializer, UserLoginSerializer, UserUpdateSerializer
from .utilities import generate_access_token, generate_refresh_token

# Create your views here.


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        User = get_user_model()

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uuid = serializer.validated_data["uuid"]
        User.objects.get_or_create(**serializer.validated_data)

        access_token = generate_access_token(uuid)
        refresh_token = generate_refresh_token(uuid)

        response = response_writer(
            "success",
            {"access_token": access_token, "refresh_token": refresh_token},
            200,
            "Created",
        )

        return Response(response, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    def patch(self, request):
        User = get_user_model()

        serializer = UserUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        uuid = request.user.uuid

        User.objects.filter(uuid=uuid).update_or_create(serializer.validated_data)

        response = response_writer(
            "success",
            User.objects.filter(uuid=uuid).values(*get_model_fields(User)),
            200,
            "Updated",
        )
        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):
        User = get_user_model()

        print(User.objects.get(uuid=request.user.uuid).delete())

        response = response_writer("success", None, 200, "Deleted")
        return Response(response, status=status.HTTP_200_OK)


class RefreshTokenAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        serializer = RefreshTokenSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        refresh_token = serializer.validated_data["refresh_token"]

        try:
            payload = jwt.decode(refresh_token, settings.SECRET_KEY, algorithms="HS256")

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
