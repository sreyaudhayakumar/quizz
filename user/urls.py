from django.urls import path
from .views import *

urlpatterns = [
     path("register/", UserListCreateView.as_view(), name="user-register"),  
    path("register/<int:id>/", UserDetailView.as_view(), name="user-detail"),
    path("login/", LoginView.as_view()),
]
