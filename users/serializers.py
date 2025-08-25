from users.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [  
            'username',
            'first_name',
            'last_name',
            'password'
        ]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user_qs = User.objects.filter(username=username)
        if not user_qs.exists():
            raise serializers.ValidationError("Invalid username or password")

        user = user_qs.first() 

        if not check_password(password, user.password):
            raise serializers.ValidationError("Invalid username or password")

        attrs['user'] = user
        return attrs
