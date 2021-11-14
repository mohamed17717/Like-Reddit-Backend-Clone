from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import IsAdminUser

from core.generics import ToggleRecordGenericView
from threads.models import Thread, ThreadPin

from threads.serializers import Thread_AdminUpdateState_Serializer, ThreadPinSerializer 


class ThreadPin_List_ApiView(ListAPIView):
  queryset = ThreadPin.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = ThreadPinSerializer

class ThreadPin_Toggle_ApiView(ToggleRecordGenericView):
  model = ThreadPin
  lookup_field = 'thread_id'
  permission_classes = [IsAdminUser]

  def get_queryset_kwargs(self, request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return {'thread': thread}

class Thread_AdminUpdateState_ApiView(RetrieveUpdateAPIView):
  queryset = Thread.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = Thread_AdminUpdateState_Serializer

  lookup_field = 'pk'
  lookup_url_kwarg = 'thread_id'


