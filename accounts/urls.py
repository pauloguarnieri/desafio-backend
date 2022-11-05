from django.contrib import admin
from django.urls import path
from accounts import views


urlpatterns = [
    path('accounts/register/', views.AccountView.as_view()),
]
