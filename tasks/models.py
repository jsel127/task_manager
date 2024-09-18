from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")