from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='user-create'),
    path('token/', views.CreateTokenView.as_view(), name='user-token'),
    path('me/', views.ManageUserView.as_view(), name='user-me'),
]
