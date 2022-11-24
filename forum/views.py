from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import QuastionSerializer, AnswerSerializer
from .models import Quastion, Answer


class QuastionListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Quastion.objects.all()
    serializer_class = QuastionSerializer

#
# class QuastionCreateView(CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Quastion.objects.all()
#     serializer_class = QuastionSerializer


class QuastionDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Quastion.objects.all()
    serializer_class = QuastionSerializer


class AnswerListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


# class AnswerCreateView(CreateAPIView):
#     permission_classes = (IsAuthenticated,)
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer


class AnswerDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
