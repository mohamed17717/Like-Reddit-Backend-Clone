from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
  type = serializers.CharField(source='type.type')
  msg = serializers.CharField(source='message')
  class Meta:
    model = Notification
    fields = ('msg', 'created', 'is_viewed', 'type', )

