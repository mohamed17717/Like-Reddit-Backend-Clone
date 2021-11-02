from rest_framework import views

from notifications.models import Notification
from notifications.serializers import NotificationSerializer
from rest_framework.pagination import LimitOffsetPagination

class Notification_ListOwn_ApiView(views.APIView, LimitOffsetPagination):
  ''' List his own notifications only order_by created '''

  def get(self, request, **kwargs):
    qs = Notification.objects.filter(user=request.user)
    results = self.paginate_queryset(qs, request, view=self)

    serializer = NotificationSerializer(results, many=True)

    return self.get_paginated_response(serializer.data)



