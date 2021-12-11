from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsUserNotBanned
from posts.models import Post

from posts.serializers import PostSerializer


class Post_CreateReplay_ApiView(CreateAPIView):
  serializer_class = PostSerializer
  permission_classes = [IsAuthenticated, IsUserNotBanned]

  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'

  def get_serializer_context(self):
    context = super(Post_CreateReplay_ApiView, self).get_serializer_context()

    post_id = self.kwargs.get(self.lookup_url_kwarg)
    comment = Post.objects.one_alive(pk=post_id)
    context.update({"request": self.request, 'post_type': 'replay', 'to': comment})

    return context

