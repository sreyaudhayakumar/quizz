from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user.permissions import IsAdmin
from .models import Submission
from .serializers import SubmissionSerializer


class SubmitQuizView(generics.CreateAPIView):
    """
    Handles quiz submission by authenticated users.

    Flow:
    - Reads quiz + answers from request payload
    - Automatically assigns logged-in user to Submission.user
    - Calculates the score inside serializer create()
    """
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        
        return {"request": self.request}

    def post(self, request, *args, **kwargs):
        """
        Override post() to return customized response.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        submission = serializer.save()

        return Response(
            {
                "message": "Quiz submitted successfully",
                "submission_id": submission.id,
                "score": submission.score,
            },
            status=status.HTTP_201_CREATED
        )


class MySubmissionsView(generics.ListAPIView):
    """
    Returns all submissions made by the currently logged-in user.
    """
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
    
        return Submission.objects.filter(user=self.request.user)


class AllSubmissionsView(generics.ListAPIView):
    """
    Admin-only view to retrieve all quiz submissions.
    """
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = Submission.objects.all()
