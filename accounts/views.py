from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import AccountSerializer, AccountAdminSerializer


class AccountView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AccountSerializer


class AccountAdminView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = AccountAdminSerializer