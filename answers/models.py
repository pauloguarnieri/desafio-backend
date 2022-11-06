from django.db import models

class Answer(models.Model):
    
    answer = models.CharField(max_length=100)
    is_true = models.BooleanField()

    question = models.ForeignKey('questions.Question', related_name='answers', on_delete=models.DO_NOTHING)
