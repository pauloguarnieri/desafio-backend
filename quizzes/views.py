from rest_framework.views import APIView
from questions.models import Question
from questions.serializers import QuestionSerializer
from rest_framework.response import Response
from .permissions import IsPlayerPermission
from rest_framework.authentication import TokenAuthentication
from categories.models import Category
from utils.helpers import get_random_questions
from rest_framework import status


class QuizView(APIView):

    ## permissões blokeadas para desenvolvimento

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsPlayerPermission]
    
    def post(self, request):
        #pegando o id da categoria
        categoria = Category.objects.get(id=request.data['category_id'])

        #filtrando as questões da categoria selecionada
        questions = Question.objects.filter(category=categoria)

        # if len(questions) < 10:
        #     return Response(
        #         {"message": "this category doesn't have enough questions for a new quiz"},
        #         status=status.HTTP_400_BAD_REQUEST
        #         )

        #chamando função que seleciona 10 questões aleatorias dentre as existentes
        #questions_range = len(questions)
        #random_questions = get_random_questions(questions, questions_range)

        #Chamar serializer de quiz e passar as questoes

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)