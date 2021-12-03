from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from core.permissions import IsUserNotBanned

from threads.models import Thread
from states.models import PrivacyState

from threads.serializers import Thread_Owner_serializer


class Thread_Owner_ApiView(ModelViewSet):
  permission_classes = [IsAuthenticated, IsUserNotBanned]
  serializer_class = Thread_Owner_serializer

  def get_queryset(self):
    qs = Thread.objects.filter(post__user=self.request.user)
    return qs

  def get_serializer_context(self):
    context = super(Thread_Owner_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context


class Thread_OwnerUpdateStatePrivate_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, thread_id, **kwargs):
    thread = get_object_or_404(Thread, id=thread_id)
    status = HTTP_403_FORBIDDEN
    if request.user.pk == thread.post.user.pk:
      private, _ = PrivacyState.objects.get_or_create(state='private')

      thread.privacy_state = private
      thread.save()

      status = HTTP_200_OK

    return Response(status=status)


class Thread_OwnerUpdateStatePublic_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, thread_id, **kwargs):
    thread = get_object_or_404(Thread, id=thread_id)
    status = HTTP_403_FORBIDDEN
    if request.user.pk == thread.post.user.pk:
      public, _ = PrivacyState.objects.get_or_create(state='public')

      thread.privacy_state = public
      thread.save()

      status = HTTP_200_OK

    return Response(status=status)

