from rest_framework import serializers

class UserLoginSerializer(serializers.Serializer):
    uuid = serializers.UUIDField()

class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()
    