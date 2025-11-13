from django.contrib import admin
from .models import Submission, UserAnswer


class UserAnswerInline(admin.TabularInline):
    """Show user answers within the submission admin"""
    model = UserAnswer
    extra = 0
    readonly_fields = ("question", "selected_option")  # prevent editing history


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "quiz", "score", "submitted_at")
    list_filter = ("quiz", "user")
    search_fields = ("user__username", "quiz__title")
    readonly_fields = ("score", "submitted_at")
    inlines = [UserAnswerInline]  # Nested answers


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ("submission", "question", "selected_option")
    list_filter = ("question", "selected_option")
    search_fields = (
        "submission__user__username",
        "question__text",
        "selected_option__text"
    )
