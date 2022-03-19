from rest_framework.routers import DefaultRouter
from posts.api.views import PostApiViewSet

# urlpatterns = [
#    path('posts/', APIView.as_view())
# ]

router_posts = DefaultRouter()
router_posts.register(prefix='posts', basename='posts', viewset=PostApiViewSet)
