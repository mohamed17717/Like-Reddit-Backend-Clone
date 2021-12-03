from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsUserNotBanned

from threads.serializers import ThreadPost_Serializer


class Thread_Commenting_ApiView(CreateAPIView):
  permission_classes = [IsAuthenticated, IsUserNotBanned]
  serializer_class = ThreadPost_Serializer

  lookup_field = 'pk'
  lookup_url_kwarg = 'thread_id'

  def get_serializer_context(self):
    context = super(Thread_Commenting_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context

