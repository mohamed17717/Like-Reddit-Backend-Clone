from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser

from posts.models import Post
from posts.serializers import Post_UpdateState_serializer


class Post_AdminUpdateState_ApiView(RetrieveUpdateAPIView):
  queryset = Post.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = Post_UpdateState_serializer

  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'

