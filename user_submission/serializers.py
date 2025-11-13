from rest_framework import serializers
from .models import Submission, UserAnswer, Option

"""Serializers for Submission and UserAnswer models."""

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ["question", "selected_option"]


class SubmissionSerializer(serializers.ModelSerializer):
    answers = UserAnswerSerializer(many=True)

    class Meta:
        model = Submission
        fields = ["id", "quiz", "score", "submitted_at", "answers"]
        read_only_fields = ["score", "submitted_at"]

    def create(self, validated_data):
        answers = validated_data.pop("answers")
        request = self.context["request"]

        submission = Submission.objects.create(
            user=request.user,
            quiz=validated_data["quiz"]
        )

        score = sum(
            1 for ans in answers if Option.objects.get(id=ans["selected_option"].id).is_correct
        )

        submission.score = score
        submission.save()

        UserAnswer.objects.bulk_create([
            UserAnswer(submission=submission, **ans) for ans in answers
        ])

        return submission

