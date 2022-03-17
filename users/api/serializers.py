from rest_framework.serializers import ModelSerializer
from users.models import User


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__' || Esto no es la mejor forma de hacerlo porque pueden haber veces que no queramos utilizar
        # todos los campos en una peticion
        fields = ['id', 'email', 'username', 'password']

    def create(self, validated_data):
        """
        Overriding create method so it encrypts the password
        """
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(ModelSerializer):
    """
    Serializer for user that returns their data but the password
    """

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name']
