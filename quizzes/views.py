from rest_framework.views import APIView
from questions.models import Question
from questions.serializers import QuestionSerializer
from rest_framework.response import Response
class QuizView(APIView):
    
    def post(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)