from django.urls import path
from .views import *

urlpatterns = [
    path("quastions/<int:pk>/", QuastionDetailView.as_view()),

    # path("quastions/create/", QuastionCreateView.as_view()),

    path("quastions/", QuastionListView.as_view()),
    path("answer/<int:pk>/", AnswerDetailView.as_view()),

    # path("answer/create/", AnswerCreateView.as_view()),

    path("answer/", AnswerListView.as_view()),
]
