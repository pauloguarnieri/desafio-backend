from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'is_player', 'is_superuser']
        read_only_fields = ['total_score', 'created_at']
        extra_kwargs = {'password': {'write_only': True}, 'is_player':{'default': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class AccountAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'email', 'is_player', 'is_superuser']
        read_only_fields = ['total_score', 'created_at']
        extra_kwargs = {'password': {'write_only': True}, 'is_player':{'default':False}, 'is_superuser':{'default': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)