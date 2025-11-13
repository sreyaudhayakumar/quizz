from django.db import models
from user.models import User
from quiz.models import Question, Option, Quiz

"""Model to store user submissions for quizzes."""

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} → {self.quiz.title} ({self.score})"

"""Model to store user's answers for each question in a submission."""

class UserAnswer(models.Model):  
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name="answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.question.text} → {self.selected_option.text}"
