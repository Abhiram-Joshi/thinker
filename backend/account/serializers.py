from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    name = serializers.CharField()
    email = serializers.EmailField()
    photo_url = serializers.URLField()

class UserUpdateSerializer(serializers.Serializer):
    name = serializers.CharField()
    bio = serializers.CharField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
