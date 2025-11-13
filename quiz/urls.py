from django.urls import path
from .views import *

urlpatterns = [
    path("categories/", CategoryListCreateView.as_view()),
    path("categories/<int:pk>/", CategoryUpdateDeleteView.as_view()),

    path("admin/", QuizListCreateView.as_view()),
    path("admin/<int:pk>/", QuizUpdateDeleteView.as_view()),

    path("admin/add-question/", QuestionCreateView.as_view()),

    path("active/", ActiveQuizListView.as_view()), 
]
