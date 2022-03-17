from django.db import models
from categories.models import Category
from users.models import User


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    body = models.TextField()
    category = models.ManyToManyField(Category)
