from .models import Question
from rest_framework import serializers
from answers.serializers import AnswerCreationSerializer
from categories.serializers import CategorySerializer
from categories.models import Category
from answers.models import Answer
import ipdb

class QuestionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Question
        fields = ['id', 'question', 'category', 'answers']
        read_only_fields = ['id']
    
    category =  CategorySerializer()
    answers =  AnswerCreationSerializer(many=True)
    
    def create(self, validated_data):
        #separando categoria e respostas
        category_poped = validated_data.pop('category')
        answers_poped = validated_data.pop('answers')

        #salvando questão e categoria
        validated_category, _ = Category.objects.get_or_create(**category_poped)
        question, _ = Question.objects.get_or_create(**validated_data, category=validated_category)

        #salvando respostas
        for item in answers_poped:
            validated_answer, _ = Answer.objects.get_or_create(**item, question=question)
            question.answers.add(validated_answer)

        return question