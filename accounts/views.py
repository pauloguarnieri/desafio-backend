
from .serializers import LoginSerializer, AccountSerializer, AccountAdminSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from .models import User


class AccountView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AccountSerializer

    def perform_create(self, serializer):
        return serializer.save()


class AccountAdminView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AccountAdminSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username = serializer.validated_data['username'],
            password = serializer.validated_data['password']
            )

        if user: 
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        
        return Response(
            {"detail":"invalid username or password"},
            status=status.HTTP_401_UNAUTHORIZED
            )