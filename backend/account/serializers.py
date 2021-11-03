from rest_framework import serializers


class UserLoginSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()
    name = serializers.CharField()
    email = serializers.EmailField()
    photo_url = serializers.URLField()


class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
