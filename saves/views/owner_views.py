from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.generics import ToggleRecordGenericView

from posts.models import Post
from saves.models import SavePost
from saves.serializers import SavePostSerializer


class SavePost_ToggleSave_ApiView(ToggleRecordGenericView):
  model = SavePost
  permission_classes = [IsAuthenticated]

  def get_queryset_kwargs(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return {'user': request.user, 'post': post}


class SavePost_ListSaves_ApiView(ListAPIView):
  serializer_class = SavePostSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    qs = SavePost.objects.filter(user=self.request.user, post__existing_state='active')
    return qs


