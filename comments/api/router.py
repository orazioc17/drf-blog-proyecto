from django.urls import path
from users.api.views import APIView

urlpatterns = [
    path('posts/', APIView.as_view())
]
