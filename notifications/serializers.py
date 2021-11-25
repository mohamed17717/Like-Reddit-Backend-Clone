from rest_framework import serializers
from notifications.models import NotificationType, NotificationMessage, Notification, NotificationSender


class NotificationTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = NotificationType
    fields = '__all__'


class NotificationMessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = NotificationMessage
    fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
  type = serializers.CharField(source='type.type')
  msg = serializers.CharField(source='message')
  class Meta:
    model = Notification
    fields = ('msg', 'created', 'is_viewed', 'type', )


class NotificationSenderSerializer(serializers.ModelSerializer):
  class Meta:
    model = NotificationSender
    fields = '__all__'

