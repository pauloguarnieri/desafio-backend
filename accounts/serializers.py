from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'is_player', 'is_superuser', 'password']
        read_only_fields = ['total_score', 'date_joine']
        extra_kwargs = {'password': {'write_only': True}, 'is_player':{'default': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AccountAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'is_player', 'is_superuser', 'password']
        read_only_fields = ['total_score', 'date_joined']
        extra_kwargs = {'password': {'write_only': True}, 'is_player':{'default':False}, 'is_superuser':{'default': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)