from django.urls import path
from .views import SubmitQuizView, MySubmissionsView, AllSubmissionsView

urlpatterns = [
    path("submit/", SubmitQuizView.as_view()),
    path("my/", MySubmissionsView.as_view()),
    path("admin/all/", AllSubmissionsView.as_view()),
]
