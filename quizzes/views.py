from rest_framework.views import APIView
from questions.models import Question
from questions.serializers import QuestionSerializer
from rest_framework.response import Response
from .permissions import IsPlayerPermission
from rest_framework.authentication import TokenAuthentication


class QuizView(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPlayerPermission]
    
    def post(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)