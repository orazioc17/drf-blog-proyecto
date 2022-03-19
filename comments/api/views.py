from rest_framework.viewsets import ModelViewSet
from comments.api.serializers import CommentSerializer
from comments.models import Comment


class CommentApiViewSet(ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    serializer_class = CommentSerializer
    # queryset = Category.objects.all()
    queryset = Comment.objects.all()
    # lookup_field = 'slug'  # Con esto los metodos POST, PUT, PATCH y DELETE dejan de usar el id y usaran el field slug
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title']  # De esta manera se pueden filtrar en los requests mediante query params