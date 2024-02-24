from django.contrib import admin

from recipe.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass
