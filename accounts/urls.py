from django.contrib import admin
from django.urls import path
from accounts import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('accounts/player/register/', views.AccountView.as_view()),
    path('accounts/admin/register/', views.AccountAdminView.as_view()),
    path('accounts/login/', obtain_auth_token, name="login")
]   
