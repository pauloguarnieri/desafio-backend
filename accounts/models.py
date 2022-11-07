from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    # password = models.CharField(max_length=20)
    is_player = models.BooleanField(null=True)
    total_score = models.PositiveIntegerField(blank=True, null=True, default=0)

    REQUIRED_FIELDS: list[str] = ['email', 'first_name', 'last_name']