from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class Notification_ListOwn_ApiView(ListAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = NotificationSerializer

  def get_queryset(self):
    return Notification.objects.filter(user=self.request.user)

