from django.urls import path, include
from rest_framework.routers import DefaultRouter
from recipe import views

app_name = 'recipe'
router = DefaultRouter()
router.register('recipe', views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls))
]