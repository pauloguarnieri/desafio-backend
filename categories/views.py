from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView
from quizzes.permissions import IsPlayerPermission
from .serializers import CategorySerializer
from .models import Category


class CategoryView(ListAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPlayerPermission]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
