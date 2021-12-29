
from django.urls import reverse
from rest_framework import serializers
from accounts.serializers import UserBasicPublicSerializer
from posts.serializers import PostSerializer
from reports.models import ReportDecision, ReportType, ReportSubType, PostReport


class ReportDecisionSerializer(serializers.ModelSerializer):
  class Meta:
    model = ReportDecision
    fields = '__all__'


class ReportTypeSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='get_absolute_url', read_only=True)
  class Meta:
    model = ReportType
    fields = ('title', 'description', 'url')


class ReportSubTypeSerializer(serializers.ModelSerializer):
  main_type = serializers.CharField(source='type.title', read_only=True)
  type_id = serializers.IntegerField(write_only=True)
  class Meta:
    model = ReportSubType
    fields = ('id', 'title', 'description', 'main_type', 'type_id')


class PostReportSerializer(serializers.ModelSerializer):
  decision_urls = serializers.SerializerMethodField(read_only=True)
  user = UserBasicPublicSerializer(read_only=True)
  post = PostSerializer(read_only=True)
  decision = serializers.CharField(source='decision.name')
  type = ReportSubTypeSerializer(read_only=True)

  def get_decision_urls(self, obj):
    types = ['pending', 'safe', 'warn', 'dangerous']
    urls = {}
    for t in types:
      urls[t] = reverse(f'reports:update-report-decision-{t}', kwargs={'report_id': obj.pk})
    
    return urls

  class Meta:
    model = PostReport
    fields = ('id', 'type', 'user','post', 'decision', 'decision_urls')


