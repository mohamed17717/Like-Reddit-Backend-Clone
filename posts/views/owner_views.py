from rest_framework.permissions import IsAuthenticated

from core.generics import UpdateDestroyListRetrieveViewSet

from posts.models import Post
from posts.serializers import PostSerializer


class Post_OwnerActions_ApiView(UpdateDestroyListRetrieveViewSet):
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    qs = Post.objects.all_for_owner(self.request.user)
    return qs

