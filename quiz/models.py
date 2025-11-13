from django.db import models
from user.models import User

"""create category for admin to create quiz under specific category"""
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

"""create quiz under specific category with questions and options"""
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="quizzes")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

"""create questions under specific quiz with options"""
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=400)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.text

"""create options under specific question with is_correct field"""
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  

    def __str__(self):
        return self.text
