from rest_framework.serializers import ModelSerializer
from categories.models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__' || Esto no es la mejor forma de hacerlo porque pueden haber veces que no queramos utilizar
        # todos los campos en una peticion
        fields = ['id', 'title', 'slug', 'published']
