from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostReplaySerializer


class PostReplay_ListPostReplays_ApiView(APIView):
  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'
  permission_classes = [AllowAny]

  def get(self, request, post_id):
    post = Post.objects.one_alive(pk=post_id)
    serialized = PostReplaySerializer(post.replays.all_alive(), many=True)

    return Response(serialized.data)
