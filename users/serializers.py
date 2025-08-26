from users.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
# from django.contrib.auth.hashers import check_password
# from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
        user = User(
            username=validated_data["username"]
        )
        user.set_password(validated_data["password"])  # 👈 muhim: hash saqlash
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if not user.is_active:
                raise serializers.ValidationError("User is inactive.")
            data["user"] = user
            return data

        raise serializers.ValidationError("Invalid username or password.")