from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from reports.models import PostReport, ReportSubType, ReportType
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

class PostReport_UserReport_Apiview(APIView):
  serializer_class = PostReportSerializer
  permission_classes = [IsAuthenticated]

  def get(self, request, post_id, type_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)
    report_type = get_object_or_404(ReportSubType, id=type_id)

    report = PostReport.objects.create(user=user, post=post, type=report_type)
    return Response(self.serializer_class(report).data)

