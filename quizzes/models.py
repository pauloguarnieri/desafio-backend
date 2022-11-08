from django.db import models

class Quiz(models.Model):
    
    category_id = models.IntegerField()
    
    questions = models.ManyToManyField(
        'questions.Question', 
        related_name='quizzes'
        )
    

