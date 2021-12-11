from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer


class PostReplay_ListPostReplays_ApiView(APIView, LimitOffsetPagination):
  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'
  permission_classes = [AllowAny]

  def get(self, request, post_id):
    post = Post.objects.one_alive(pk=post_id)
    replays = post.replays.all_alive()

    results = self.paginate_queryset(replays, request, view=self)
    serializer = PostSerializer(results, many=True)

    return self.get_paginated_response(data=serializer.data)

