from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.TextField()
    keywords = models.TextField()

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField(default=0)
