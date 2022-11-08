from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import QuestionSerializer
from .models import Question
from .permissions import IsAdminPermission
from rest_framework.authentication import TokenAuthentication

class QuestionView(CreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminPermission]

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer