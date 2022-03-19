from rest_framework.serializers import ModelSerializer
from comments.models import Comment
from users.api.serializers import UserSerializer
from posts.api.serializers import PostSerializer


class CommentSerializer(ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        # fields = '__all__' || Esto no es la mejor forma de hacerlo porque pueden haber veces que no queramos utilizar
        # todos los campos en una peticion
        fields = ['text', 'created_at', 'user', 'post']
