
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



class PostReport_Create_Serializer(serializers.ModelSerializer):
  class Meta:
    model = PostReport
    fields = ('id', 'type', 'user','post',)

    extra_kwargs = {
      'user': {'read_only': True},
      'post': {'read_only': True},
    }

class PostReport_UpdateDecision_Serializer(serializers.ModelSerializer):
  class Meta:
    model = PostReport
    fields = ('id', 'decision',)



