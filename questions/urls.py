
from django.urls import path, include
from questions import views

urlpatterns = [
    path('questions/', views.QuestionView.as_view()),

]
