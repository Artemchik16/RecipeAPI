from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path("admin/", admin.site.urls),
    # apps
    path('api/users/', include('users.urls', namespace='users')),
    path('api/recipe/', include('recipe.urls', namespace='recipe')),
    # documentation
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
