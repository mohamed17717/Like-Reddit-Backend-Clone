from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView

from posts.models import Post
from reports.models import ReportSubType, ReportType
from reports.serializers import (
  PostReport_Create_Serializer,
  ReportSubTypeSerializer,
  ReportTypeSerializer
)


class ReportType_UserList_ApiView(ListAPIView):
  queryset = ReportType.objects.all()
  serializer_class = ReportTypeSerializer
  permission_classes = [IsAuthenticated]
  paginator = None


class ReportSubType_UserList_ApiView(ListAPIView):
  queryset = ReportSubType.objects.all()
  serializer_class = ReportSubTypeSerializer
  permission_classes = [IsAuthenticated]
  paginator = None


class PostReport_UserReport_Apiview(CreateAPIView):
  serializer_class = PostReport_Create_Serializer
  lookup_field = 'post_id'
  permission_classes = [IsAuthenticated]

  def perform_create(self, serializer):
    user = self.request.user

    post_id = self.kwargs.get(self.lookup_field, '')
    post = get_object_or_404(Post, id=post_id)

    serializer.save(user=user, post=post)

