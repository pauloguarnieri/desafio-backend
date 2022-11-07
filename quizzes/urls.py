from django.urls import path, include
from quizzes import views

urlpatterns = [
    path('quiz/', views.QuizView.as_view()),
]