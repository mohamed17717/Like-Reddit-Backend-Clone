from django.db.models.expressions import F
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from categories.models import SubCategory
from core.permissions import IsUserHasAccessToThisContent

from threads.models import Thread
from threads.serializers import (
  Thread_BasicInfo_Serializer,
  Thread_FullInfo_Serializer
)


class Thread_Retrieve_ApiView(RetrieveAPIView):
  serializer_class = Thread_FullInfo_Serializer
  permission_classes = [AllowAny]

  lookup_field = 'pk'
  lookup_url_kwarg = 'thread_id'

  def get(self, request, *args, **kwargs):
    pk = kwargs[self.lookup_url_kwarg]
    thread = Thread.objects.one_alive(pk=pk)

    IsUserHasAccessToThisContent(request, thread)

    Thread.objects.select_for_update().filter(pk=pk).update(visits_count=F('visits_count') + 1)

    serialized = self.serializer_class(thread)
    return Response(serialized.data)


class Thread_ListOnSubCategory_ApiView(APIView, LimitOffsetPagination):
  permission_classes = [AllowAny]

  def get(self, request, sub_category_id):
    sub_category = get_object_or_404(SubCategory, id=sub_category_id)

    IsUserHasAccessToThisContent(request, sub_category)

    threads = sub_category.threads.all_alive()
    results = self.paginate_queryset(threads, request, view=self)

    serializer = Thread_BasicInfo_Serializer(results, many=True)
    return self.get_paginated_response(data=serializer.data)


class Thread_LatestList_ApiView(ListAPIView):
  queryset = Thread.objects.all_alive()
  serializer_class = Thread_BasicInfo_Serializer
  permission_classes = [AllowAny]

class ThreadPin_CommonPinnedThreads_ApiView(ListAPIView):
  queryset = Thread.objects.all_alive().filter(pinned__isnull=False)
  serializer_class = Thread_BasicInfo_Serializer
  permission_classes = [AllowAny]
class ThreadPin_ListOnSubCategory_ApiView(APIView, LimitOffsetPagination):
  permission_classes = [AllowAny]
  serializer_class = Thread_BasicInfo_Serializer

  def get(self, request, sub_category_id):
    sub_category = get_object_or_404(SubCategory, id=sub_category_id)

    IsUserHasAccessToThisContent(request, sub_category)

    threads = Thread.objects.all_alive().filter(pinned__isnull=False, category=sub_category)
    results = self.paginate_queryset(threads, request, view=self)

    serializer = self.serializer_class(results, many=True)
    return self.get_paginated_response(data=serializer.data)
