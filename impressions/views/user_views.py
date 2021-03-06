from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from rest_framework.response import Response

from core.generics import ToggleRecordGenericView

from impressions.models import Emoji, PostDownVote, PostEmoji, PostUpVote
from posts.models import Post
from impressions.serializers import EmojiSerializer


class Emoji_UserList_ApiView(ListAPIView):
  queryset = Emoji.objects.all()
  serializer_class = EmojiSerializer
  permission_classes = [IsAuthenticated]

  paginator = None


class PostEmoji_UserReact_ApiView(ToggleRecordGenericView):
  model = PostEmoji
  permission_classes = [IsAuthenticated]

  def get_queryset_kwargs(self, request, post_id, emoji_id):
    post = get_object_or_404(Post, id=post_id)
    emoji = get_object_or_404(Emoji, id=emoji_id)

    return {'user': request.user, 'post': post, 'emoji': emoji}


# ------------------- Abstract Upvote Downvote ------------------------#
class Abstract_UpvoteDownvote_ApiView(APIView):
  permission_classes = [IsAuthenticated]
  model = None # required
  inverse_model = None # required

  def get(self, request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    self.inverse_model.objects.filter(post=post, user=user).delete()
    self.model.objects.create(post=post, user=user)

    return Response(status=HTTP_201_CREATED)

  def delete(self, request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    reaction = get_object_or_404(self.model, post=post, user=user)
    reaction.delete()

    return Response(status=HTTP_204_NO_CONTENT)

class PostUpVote_UserReact_ApiView(Abstract_UpvoteDownvote_ApiView):
  model = PostUpVote
  inverse_model = PostDownVote

class PostDownVote_UserReact_ApiView(Abstract_UpvoteDownvote_ApiView):
  model = PostDownVote
  inverse_model = PostUpVote
