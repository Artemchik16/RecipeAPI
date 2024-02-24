from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import authentication, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users import serializers


@extend_schema_view(
    post=extend_schema(summary="Registration", tags=["Register & Authentication"]),
)
class CreateUserView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class CreateTokenView(ObtainAuthToken):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
