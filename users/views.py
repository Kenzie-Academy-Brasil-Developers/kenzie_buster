from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import RegisterSerializer
from .serializers import CustomJWTSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404
from .permissions import GetUserPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class RegisterView(APIView):
    def get(self, request: Request) -> Response:
        return Response("")

    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class LoginJWTView(TokenObtainPairView):
    serializer_class = CustomJWTSerializer


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [GetUserPermissions]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
