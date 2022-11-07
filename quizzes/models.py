from django.db import models

class Quiz(models.Model):
    
    category_id = models.IntegerField()
    # created_by = models.CharField(max_length=255)

    questions = models.ManyToManyField('questions.Question', related_name='quizzes')
    

