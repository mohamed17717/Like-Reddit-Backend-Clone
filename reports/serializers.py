
from rest_framework import serializers
from reports.models import ReportDecision, ReportType, ReportSubType, PostReport


class ReportDecisionSerializer(serializers.ModelSerializer):
  class Meta:
    model = ReportDecision
    fields = '__all__'


class ReportTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ReportType
    fields = '__all__'


class ReportSubTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = ReportSubType
    fields = '__all__'


class PostReportSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostReport
    fields = '__all__'

