from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Choice(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
      
class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    question=models.CharField(max_length=2048,null=True)
    selections=models.ManyToManyField(Choice)
    
    def __str__(self):
        return self.question
