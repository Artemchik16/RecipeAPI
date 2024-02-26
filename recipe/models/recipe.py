import os
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models


def recipe_image_file_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid4()}{ext}'
    return os.path.join('uploads', 'recipe', filename)


class Recipe(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(to='recipe.Tag')
    ingredient = models.ManyToManyField(to='recipe.Ingredient')
    image = models.ImageField(upload_to=recipe_image_file_path, null=True, blank=True)

    def __str__(self):
        return self.title
