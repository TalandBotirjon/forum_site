
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quastion(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    asked = models.TextField()

    asked_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}. {self.asked}"


class Answer(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Quastion, on_delete=models.CASCADE)
    reply = models.TextField()
    answer_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.question.id}. Javob: {self.reply}"


