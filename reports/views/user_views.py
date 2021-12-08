from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from reports.models import ReportSubType, ReportType
from reports.serializers import PostReportSerializer, ReportSubTypeSerializer, ReportTypeSerializer


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
  lookup_url_kwarg = 'type_id'

  def get(self, request, **kwargs):
    type_id = kwargs.get(self.lookup_url_kwarg)
    obj = get_object_or_404(ReportType, pk=type_id)

    sub_types = ReportSubTypeSerializer(obj.sub_types, many=True)

    return Response(sub_types.data)

class PostReport_UserReport_Apiview(CreateAPIView):
  serializer_class = PostReportSerializer
  permission_classes = [IsAuthenticated]

  lookup_field = 'pk'
  lookup_url_kwarg = 'post_id'

  def perform_create(self, serializer):
    user = self.request.user

    post_id = self.kwargs.get(self.lookup_url_kwarg, '')
    post = get_object_or_404(Post, id=post_id)

    serializer.save(user=user, post=post)

