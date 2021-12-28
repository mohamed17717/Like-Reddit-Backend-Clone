from rest_framework import serializers

from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='sender.sender_object.get_notification_url')
  message = serializers.CharField(source='sender.sender_object.get_notification_message')

  class Meta:
    model = Notification
    fields = ('message', 'created', 'is_viewed', 'url', )

