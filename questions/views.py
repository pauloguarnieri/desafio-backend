from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import QuestionSerializer
from .models import Question

class QuestionView(CreateAPIView):

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer