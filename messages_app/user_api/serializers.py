from rest_framework import serializers as rfs
from .models import UsersProfile

class UsersSerializer(rfs.ModelSerializer):
    """Serializes a user"""
    class Meta:
        model = UsersProfile
        fields = ('id', 'email')


class UserLoginSerializer(rfs.Serializer):
    email = rfs.EmailField(write_only=True)
    password = rfs.CharField(write_only=True)
    """Serializes a login user"""
    class Meta:
        fields = ('email', 'password')


class UserCreateSerializer(rfs.Serializer):
    email = rfs.EmailField(write_only=True)
    name = rfs.CharField(write_only=True)
    """Serializes a create user"""
    class Meta:
        fields = ('email', 'name')


class UserTokenSerializer(rfs.ModelSerializer):
    """Serializes a token """
    class Meta:
        model = UsersProfile
        fields = ('id', 'auth_token')

    






  