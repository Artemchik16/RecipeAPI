from recipe.models import Recipe
from django.contrib import admin


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
