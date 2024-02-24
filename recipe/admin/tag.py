from django.contrib import admin

from recipe.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
