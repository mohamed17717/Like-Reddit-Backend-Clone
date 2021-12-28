from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView

from rest_framework.permissions import IsAdminUser
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.response import Response

from core.generics import ToggleRecordGenericView
from threads.models import Thread, ThreadPin

from threads.serializers import (
  Thread_BasicInfo_Serializer,
  Thread_ReadPendingState_Serializer,
  Thread_WritePendingState_Serializer
)


class ThreadPin_List_ApiView(ListAPIView):
  queryset = Thread.objects.all_alive().filter(pinned__isnull=False)
  permission_classes = [IsAdminUser]
  serializer_class = Thread_BasicInfo_Serializer

class Thread_ListPending_ApiView(ListAPIView):
  queryset = Thread.objects.all_pending()
  permission_classes = [IsAdminUser]
  serializer_class = Thread_ReadPendingState_Serializer


class ThreadPin_Toggle_ApiView(ToggleRecordGenericView):
  model = ThreadPin
  permission_classes = [IsAdminUser]

  def get_queryset_kwargs(self, request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return {'thread': thread}


# ---------- Update pending state for thread ---------- #

class Thread_Abstract_AdminUpdatePendingState_ApiView(APIView):
  serializer_class = Thread_WritePendingState_Serializer  
  update_state_value = None # required

  def get(self, request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    data = {'pending_state': self.update_state_value}

    serializer = self.serializer_class(data=data)
    serializer.is_valid(raise_exception=True)

    serializer.update(thread, data)

    return Response(status=HTTP_204_NO_CONTENT)

class Thread_AdminAcceptPendingState_ApiView(Thread_Abstract_AdminUpdatePendingState_ApiView):
  update_state_value = 'accept'

class Thread_AdminRejectPendingState_ApiView(Thread_Abstract_AdminUpdatePendingState_ApiView):
  update_state_value = 'declined'

