from django.urls import path
from accounts import views


urlpatterns = [
    path('accounts/player/register/', views.AccountView.as_view()),
    path('accounts/admin/register/', views.AccountAdminView.as_view()),
    path('accounts/login/', views.LoginView.as_view()),
]   
