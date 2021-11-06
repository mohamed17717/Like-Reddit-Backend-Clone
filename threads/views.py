from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from categories.models import SubCategory
from core.generics import ToggleRecordGenericView
from threads.models import Thread, ThreadPin, ThreadState

from threads.serializers import Thread_AdminUpdateState_Serializer, Thread_ListThreadsInSubCategoryPage_serializer, Thread_Owner_serializer, ThreadPinSerializer, ThreadPost_Serializer 


class Thread_Owner_ApiView(ModelViewSet):
  permission_classes = [IsAuthenticated]
  serializer_class = Thread_Owner_serializer

  def get_queryset(self):
    qs = Thread.objects.filter(post__user=self.request.user)
    return qs

  def get_serializer_context(self):
    context = super(Thread_Owner_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context

class Thread_Retrieve_ApiView(RetrieveAPIView):
  queryset = Thread.objects.all()
  serializer_class = Thread_Owner_serializer


class Thread_ListOnSubCategory_ApiView(APIView, LimitOffsetPagination):
  def get(self, request, sub_category_id):
    sub_category = get_object_or_404(SubCategory, id=sub_category_id)
    threads = sub_category.threads.all()
    results = self.paginate_queryset(threads, request, view=self)

    serializer = Thread_ListThreadsInSubCategoryPage_serializer(results, many=True)
    return self.get_paginated_response(data=serializer.data)


class ThreadPin_Toggle_ApiView(ToggleRecordGenericView):
  model = ThreadPin
  lookup_field = 'thread_id'
  permission_classes = [IsAdminUser]

  def get_queryset_kwargs(self, request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return {'thread': thread}


class ThreadPin_List_ApiView(ListAPIView):
  queryset = ThreadPin.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = ThreadPinSerializer


class Thread_AdminUpdateState_ApiView(RetrieveUpdateAPIView):
  queryset = Thread.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = Thread_AdminUpdateState_Serializer


class Thread_OwnerUpdateStatePrivate_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, thread_id, **kwargs):
    thread = get_object_or_404(Thread, id=thread_id)
    status = HTTP_403_FORBIDDEN
    if request.user.pk == thread.post.user.pk:
      private, _ = ThreadState.objects.get_or_create(state='private')

      thread.state = private
      thread.save()

      status = HTTP_200_OK

    return Response(status=status)


class Thread_OwnerUpdateStatePublic_ApiView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, thread_id, **kwargs):
    thread = get_object_or_404(Thread, id=thread_id)
    status = HTTP_403_FORBIDDEN
    if request.user.pk == thread.post.user.pk:
      public, _ = ThreadState.objects.get_or_create(state='public')

      thread.state = public
      thread.save()

      status = HTTP_200_OK

    return Response(status=status)




class Thread_Commenting_ApiView(CreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = ThreadPost_Serializer

  def get_serializer_context(self):
    context = super(Thread_Commenting_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context

