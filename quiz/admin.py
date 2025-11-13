from django.contrib import admin
from .models import Category, Quiz, Question, Option


class OptionInline(admin.TabularInline):
    """Inline options inside question admin"""
    model = Option
    extra = 0
    min_num = 4
    max_num = 4


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "quiz", "is_active")
    list_filter = ("quiz", "is_active")
    search_fields = ("text",)
    inlines = [OptionInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0
    fields = ("text", "is_active")


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_active")
    search_fields = ("title",)
    list_filter = ("category", "is_active")
    inlines = [QuestionInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by", "is_active")
    search_fields = ("name",)
    list_filter = ("is_active",)

