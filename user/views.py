from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegisterSerializer, LoginSerializer
from .models import User


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    lookup_field = "id"



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        tokens = RefreshToken.for_user(user)
        return Response({
            "refresh": str(tokens),
            "access": str(tokens.access_token),
            "role": user.role,
        })
