from rest_framework import serializers

from recipe.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
