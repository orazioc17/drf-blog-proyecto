from django.urls import path
from categories.api.views import CategoriesView

urlpatterns = [
    path('categories/', CategoriesView.as_view())
]
