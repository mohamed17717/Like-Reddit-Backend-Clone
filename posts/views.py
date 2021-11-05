from django.db.models.query import QuerySet
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from core.generics import UpdateDestroyListRetrieveViewSet
from posts.models import Post, PostReplay, PostState
from posts.serializers import Post_OwnerActions_Serializer, PostReplaySerializer, Post_UpdateState_serializer


class Post_OwnerActions_ApiView(UpdateDestroyListRetrieveViewSet):
  serializer_class = Post_OwnerActions_Serializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Post.objects.filter(user=self.request.user)


class Post_CreateReplay_ApiView(CreateAPIView):
  serializer_class = Post_OwnerActions_Serializer
  permission_classes = [IsAuthenticated]

  def get_serializer_context(self):
    context = super(Post_CreateReplay_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context

class PostReplay_ListPostReplays_ApiView(APIView):
  lookup_field = 'post_id'

  def get(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    serialized = PostReplaySerializer(post.replays.all(), many=True)

    return Response(serialized.data)


# class Post_OwnerMakePostPrivate_ApiView(APIView):
#   def get(self, request, post_id):
#     # make sure he is owner
#     post = get_object_or_404(Post, id=post_id)
#     status = HTTP_403_FORBIDDEN

#     if request.user.id == post.user.id:
#       private_state, _ = PostState.objects.get_or_create(name='private')
#       post.state = private_state
#       post.save()
#       status = HTTP_200_OK

#     return Response(status=status)

class Post_AdminUpdateState_ApiView(RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = Post_UpdateState_serializer
  lookup_field = 'pk'

