from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from posts.serializers import Post_OwnerActions_Serializer


class Post_CreateReplay_ApiView(CreateAPIView):
  serializer_class = Post_OwnerActions_Serializer
  permission_classes = [IsAuthenticated]

  def get_serializer_context(self):
    context = super(Post_CreateReplay_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context

