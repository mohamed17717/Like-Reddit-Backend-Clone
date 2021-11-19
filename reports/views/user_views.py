from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

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


class ReportSubType_UserListOnType_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, category_id):
    obj = get_object_or_404(ReportType, pk=category_id)
    sub_types = ReportSubTypeSerializer(obj.sub_types, many=True)

    return Response(sub_types.data)

class PostReport_UserReport_Apiview(CreateAPIView):
  serializer_class = PostReport_Create_Serializer
  permission_classes = [IsAuthenticated]

  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'

  def perform_create(self, serializer):
    user = self.request.user

    post_id = self.kwargs.get(self.lookup_url_kwarg, '')
    post = get_object_or_404(Post, id=post_id)

    serializer.save(user=user, post=post)

