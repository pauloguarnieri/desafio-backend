from rest_framework import serializers
from .models import Answer

class AnswerCreationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ['id', 'answer', 'is_true']
        read_only_fields = ['id']

class AnswerQuizSerializer(serializers.ModelSerializer):

    class Meta:
        Model = Answer
        fields = ['id', 'answer']
        