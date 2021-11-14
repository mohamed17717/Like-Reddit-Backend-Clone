from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.response import Response

from core.generics import ToggleRecordGenericView

from impressions.models import Emoji, PostDownVote, PostEmoji, PostUpVote
from posts.models import Post


class PostEmoji_UserReact_ApiView(ToggleRecordGenericView):
  model = PostEmoji
  permission_classes = [IsAuthenticated]
  post_lookup_field = 'post_id'
  emoji_lookup_field = 'emoji_id'

  def get_queryset_kwargs(self, request, post_id, emoji_id, **kwargs):
    post = get_object_or_404(Post, id=post_id)
    emoji = get_object_or_404(Emoji, id=emoji_id)

    return {'user': request.user, 'post': post, 'emoji': emoji}

class PostUpVote_UserReact_ApiView(APIView):
  permission_classes = [IsAuthenticated]
  model = PostUpVote
  inverse_model = PostDownVote

  def get(self, request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    self.inverse_model.objects.filter(post=post, user=user).delete()
    self.model.objects.create(post=post, user=user)

    return Response(status=HTTP_201_CREATED)


  def delete(self, request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    self.model.objects.filter(post=post, user=user).delete()
    return Response(status=HTTP_200_OK)

class PostDownVote_UserReact_ApiView(APIView):
  permission_classes = [IsAuthenticated]
  model = PostDownVote
  inverse_model = PostUpVote

  def get(self, request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    self.inverse_model.objects.filter(post=post, user=user).delete()
    self.model.objects.create(post=post, user=user)

    return Response(status=HTTP_201_CREATED)


  def delete(self, request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    self.model.objects.filter(post=post, user=user).delete()
    return Response(status=HTTP_200_OK)

