from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    # queryset = Category.objects.all()
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'  # Con esto los metodos POST, PUT, PATCH y DELETE dejan de usar el id y usaran el field slug
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']  # De esta manera se pueden filtrar en los requests mediante query params
    filterset_fields = ['category__slug']
