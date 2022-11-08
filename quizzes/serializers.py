from rest_framework import serializers

class QuizSerializer(serializers.ModelSerializer):
    ...

    def create(self, validated_data):
        ...