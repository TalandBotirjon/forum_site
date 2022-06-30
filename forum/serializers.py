

from rest_framework import serializers
from .models import Quastion, Answer
class QuastionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quastion
        fields = ("pk", 'auther', "asked", "asked_time")

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'auther', 'question', "reply", "answer_time")


