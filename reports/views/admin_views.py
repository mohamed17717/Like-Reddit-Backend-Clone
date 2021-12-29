from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_204_NO_CONTENT

from core.generics import CreateUpdateDestroyListViewSet

from reports.models import PostReport, ReportDecision, ReportType, ReportSubType
from reports.serializers import (
  PostReportSerializer, ReportDecisionSerializer, ReportTypeSerializer, ReportSubTypeSerializer
)


class ReportType_ApiView(ModelViewSet):
  queryset = ReportType.objects.all()
  serializer_class = ReportTypeSerializer
  model = ReportType

  permission_classes = [IsAdminUser]
  paginator = None

  def retrieve(self, request, pk):
    obj = get_object_or_404(self.model, pk=pk)
    sub_types = ReportSubTypeSerializer(obj.sub_types, many=True)

    return Response(sub_types.data)


class ReportSubType_ApiView(CreateUpdateDestroyListViewSet):
  queryset = ReportSubType.objects.all()
  serializer_class = ReportSubTypeSerializer

  permission_classes = [IsAdminUser]
  paginator = None


class PostReport_ListReports_ApiView(ListAPIView):
  queryset = PostReport.objects.all()
  serializer_class = PostReportSerializer
  permission_classes = [IsAdminUser]


class ReportDecision_ListDecision_ApiView(ListAPIView):
  queryset = ReportDecision.objects.all()
  serializer_class = ReportDecisionSerializer
  permission_classes = [IsAdminUser]

  paginator = None


class PostReport_UpdateDecision_Apiview(APIView):
  permission_classes = [IsAdminUser]

  def get(self, request, report_id):
    report = get_object_or_404(PostReport, pk=report_id)

    decision_string = tuple(filter(lambda i: i, request.path.split('/')))[-1]
    decision_obj= get_object_or_404(ReportDecision, name=decision_string)

    report.decision = decision_obj
    report.save()

    return Response(status=HTTP_204_NO_CONTENT)



