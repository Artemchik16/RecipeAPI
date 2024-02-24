from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipe.models import Tag
from recipe.serializers.tag import TagSerializer


class TagViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('name')
