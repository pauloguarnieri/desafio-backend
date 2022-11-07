from django.db import models

class Quiz(models.Model):
    
    category = models.CharField(max_length=50)
    

