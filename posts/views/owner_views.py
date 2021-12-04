from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from posts.serializers import Post_OwnerActions_Serializer

from core.generics import UpdateDestroyListRetrieveViewSet


class Post_OwnerActions_ApiView(UpdateDestroyListRetrieveViewSet):
  serializer_class = Post_OwnerActions_Serializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    qs = Post.objects.all_for_owner(self.request.user)
    return qs

