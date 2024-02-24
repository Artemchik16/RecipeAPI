from django.contrib import admin

from recipe.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')
