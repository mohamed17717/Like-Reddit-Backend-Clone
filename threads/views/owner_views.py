from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK

from core.permissions import IsUserNotBanned

from threads.models import Thread
from states.models import PrivacyState

from threads.serializers import Thread_Owner_serializer


class Thread_Owner_ApiView(ModelViewSet):
  permission_classes = [IsAuthenticated, IsUserNotBanned]
  serializer_class = Thread_Owner_serializer

  def get_queryset(self):
    return Thread.objects.all_for_owner(self.request.user)

  def get_serializer_context(self):
    context = super(Thread_Owner_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context


class Thread_OwnerUpdateStatePrivate_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, thread_id, **kwargs):
    thread = Thread.objects.one_for_owner(request.user, pk=thread_id)
    private, _ = PrivacyState.objects.get_or_create(state='private')

    thread.privacy_state = private
    thread.save()

    return Response(status=HTTP_200_OK)


class Thread_OwnerUpdateStatePublic_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, thread_id, **kwargs):
    thread = Thread.objects.one_for_owner(request.user, pk=thread_id)
    public, _ = PrivacyState.objects.get_or_create(state='public')

    thread.privacy_state = public
    thread.save()

    return Response(status=HTTP_200_OK)

