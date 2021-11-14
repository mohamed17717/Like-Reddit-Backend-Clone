from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import (
  Post_OwnerActions_Serializer,
  PostReplaySerializer
)


class PostReplay_ListPostReplays_ApiView(APIView):
  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'

  def get(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serialized = PostReplaySerializer(post.replays.all(), many=True)

    return Response(serialized.data)


class Post_CreateReplay_ApiView(CreateAPIView):
  serializer_class = Post_OwnerActions_Serializer
  permission_classes = [IsAuthenticated]

  def get_serializer_context(self):
    context = super(Post_CreateReplay_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context

