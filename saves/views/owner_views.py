from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from core.generics import ToggleRecordGenericView

from posts.models import Post
from saves.models import SavePost
from saves.serializers import SavePostSerializer


class SavePost_ToggleSave_ApiView(ToggleRecordGenericView):
  model = SavePost

  def get_queryset_kwargs(self, request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return {'user': request.user, 'post': post}


class SavePost_ListSaves_ApiView(APIView):
  def get(self, request, **kwargs):
    qs = SavePost.objects.filter(user=request.user, post__existing_state='active')
    serialized = SavePostSerializer(qs, many=True)

    return Response(serialized.data)


