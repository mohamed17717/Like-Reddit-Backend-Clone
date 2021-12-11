from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from core.permissions import IsUserNotBanned
from posts.serializers import PostSerializer
from threads.models import Thread


class Thread_Commenting_ApiView(CreateAPIView):
  permission_classes = [IsAuthenticated, IsUserNotBanned]
  serializer_class = PostSerializer

  lookup_field = 'pk'
  lookup_url_kwarg = 'thread_id'

  def get_serializer_context(self):
    context = super(Thread_Commenting_ApiView, self).get_serializer_context()

    thread_id = self.kwargs.get(self.lookup_url_kwarg)
    thread = Thread.objects.one_alive(pk=thread_id)

    context.update({"request": self.request, 'post_type': 'comment','to': thread})
    return context

