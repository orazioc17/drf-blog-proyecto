from rest_framework.serializers import ModelSerializer
from users.models import User


class PostSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__' || Esto no es la mejor forma de hacerlo porque pueden haber veces que no queramos utilizar
        # todos los campos en una peticion
        fields = ['username', 'email', 'first_name', 'last_name']
