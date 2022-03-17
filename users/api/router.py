from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import RegisterView

urlpatterns = [
    path('auth/register', RegisterView.as_view()),
    path('auth/login', TokenObtainPairView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view())
]
