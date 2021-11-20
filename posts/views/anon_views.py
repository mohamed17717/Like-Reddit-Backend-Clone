from django.shortcuts import get_object_or_404

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
    post = get_object_or_404(Post, id=post_id)
    serialized = PostReplaySerializer(post.replays.all(), many=True)

    return Response(serialized.data)
