from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from recipe.models import Ingredient
from recipe.serializers import IngredientSerializer


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('name')
