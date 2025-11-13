from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsAdmin
from .models import Category, Quiz, Question
from .serializers import CategorySerializer, QuizSerializer, QuestionSerializer

"""Views for managing categories, quizzes, and questions."""

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class CategoryUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class QuizUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class ActiveQuizListView(generics.ListAPIView):
    queryset = Quiz.objects.filter(is_active=True)
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]
