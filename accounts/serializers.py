from rest_framework import serializers
from .models import User

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'is_superuser', 'first_name', 'last_name', 'username', 'is_player']
        read_only_fields = ['total_score', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)