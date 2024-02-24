from django.contrib.auth import get_user_model
from django.db import models


class Recipe(models.Model):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    tags = models.ManyToManyField(to='recipe.Tag')

    def __str__(self):
        return self.title
