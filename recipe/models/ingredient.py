from django.contrib.auth import get_user_model
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
