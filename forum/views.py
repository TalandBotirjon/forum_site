from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import QuastionSerializer, AnswerSerializer
from .models import Quastion, Answer
from rest_framework import generics

class QuastionListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Quastion.objects.all()
    serializer_class = QuastionSerializer

class QuastionCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Quastion.objects.all()
    serializer_class = QuastionSerializer

class QuastionUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Quastion.objects.all()
    serializer_class = QuastionSerializer


class AnswerListView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

class AnswerUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
