from rest_framework.views import APIView
from questions.models import Question
from questions.serializers import QuestionSerializer
from rest_framework.response import Response
from .permissions import IsPlayerPermission
from rest_framework.authentication import TokenAuthentication
from categories.models import Category

class QuizView(APIView):

    ## permissões blokeadas para desenvolvimento
    
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsPlayerPermission]
    
    def post(self, request):
 
        categoria = Category.objects.get(id=request.data['category_id'])
        questions = Question.objects.filter(category=categoria)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)