from rest_framework import serializers
from .models import Category, Quiz, Question, Option

"""Serializers for Category, Quiz, Question, and Option models."""

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ["id", "text", "is_correct"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get("request")

        #  hide is_correct from user
        if request and request.method == "GET":
            data.pop("is_correct", None)

        return data


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ["id", "quiz", "text", "is_active", "options"]
        read_only_fields = ("id",)

    def create(self, validated_data):
        options = validated_data.pop("options")
        quiz_id = self.context["request"].data.get("quiz")

        if not quiz_id:
            raise serializers.ValidationError("Quiz ID is required")

        question = Question.objects.create(quiz_id=quiz_id, **validated_data)
        Option.objects.bulk_create([Option(question=question, **opt) for opt in options])
        return question


class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = ["id", "title", "category", "is_active", "questions"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "is_active"]
        read_only_fields = ("id",)

    def create(self, validated_data):
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)
