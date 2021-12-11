from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

from core.permissions import IsUserNotBanned

from threads.models import Thread
from states.models import PrivacyState

from threads.serializers import Thread_FullInfo_Serializer


class Thread_Owner_ApiView(ModelViewSet):
  permission_classes = [IsAuthenticated, IsUserNotBanned]
  serializer_class = Thread_FullInfo_Serializer

  def get_queryset(self):
    return Thread.objects.all_for_owner(self.request.user)

  def get_serializer_context(self):
    context = super(Thread_Owner_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context


# ---------------------- Abstract Update Thread state ---------------------- #

class Abstract_Thread_UpdateState_APiView(APIView):
  permission_classes = [IsAuthenticated]
  state = None # required

  def get(self, request, thread_id, **kwargs):
    thread = Thread.objects.one_for_owner(request.user, pk=thread_id)
    new_state = get_object_or_404(PrivacyState, state=self.state)

    thread.privacy_state = new_state
    thread.save()

    return Response(status=HTTP_200_OK)

class Thread_OwnerUpdateStatePrivate_ApiView(Abstract_Thread_UpdateState_APiView):
  state = 'private'
class Thread_OwnerUpdateStatePublic_ApiView(Abstract_Thread_UpdateState_APiView):
  state = 'public'

