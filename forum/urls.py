from django.urls import path
from .views import *

urlpatterns = [
    path("quastions/update/<int:pk>/", QuastionUpdateView.as_view()),
    path("quastions/create/", QuastionCreateView.as_view()),
    path("quastions/", QuastionListView.as_view()),
    path("answer/update/<int:id>/", AnswerUpdateView.as_view()),
    path("answer/create/", AnswerCreateView.as_view()),
    path("answer/", AnswerListView.as_view()),
]
