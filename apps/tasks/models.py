from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name=models.TextField()
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    important=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        ordering=['-created']
    
class SubTask(models.Model):
    name=models.TextField()
    description=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    important=models.BooleanField(default=False)
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    class Meta:
        ordering=['-created']