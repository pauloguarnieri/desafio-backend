from django.db import models

class Question(models.Model):

    question = models.CharField(max_length=255)
    
    category = models.ForeignKey('categorys.Category', related_name='questions', on_delete=models.DO_NOTHING)
