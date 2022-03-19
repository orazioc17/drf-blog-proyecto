from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from comments.api.permissions import IsOwnerOrReadAndCreateOnly


class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreateOnly]
    serializer_class = CommentSerializer
    # queryset = Category.objects.all()
    queryset = Comment.objects.all()
    # lookup_field = 'slug'  # Con esto los metodos POST, PUT, PATCH y DELETE dejan de usar el id y usaran el field slug
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']  # Asi ordena desde el comentario mas nuevo hasta el mas viejo
    filterset_fields = ['post']
