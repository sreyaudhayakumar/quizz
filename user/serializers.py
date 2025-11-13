from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Used for user registration.
    """
    password = serializers.CharField(write_only=True, min_length=4)

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "role"]

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """
    Used for JWT login authentication.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        attrs["user"] = user
        return attrs
