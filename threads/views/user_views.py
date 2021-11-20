from django.shortcuts import get_object_or_404

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from categories.models import SubCategory
from threads.models import Thread

from threads.serializers import (
  Thread_ListThreadsInSubCategoryPage_serializer,
  Thread_Owner_serializer,
  ThreadPost_Serializer,

  Thread_LatestList_Serializer
) 


class Thread_Retrieve_ApiView(RetrieveAPIView):
  queryset = Thread.objects.all()
  serializer_class = Thread_Owner_serializer

  lookup_field = 'pk'
  lookup_url_kwarg = 'thread_id'



class Thread_ListOnSubCategory_ApiView(APIView, LimitOffsetPagination):
  def get(self, request, sub_category_id):
    sub_category = get_object_or_404(SubCategory, id=sub_category_id)
    threads = sub_category.threads.all()
    results = self.paginate_queryset(threads, request, view=self)

    serializer = Thread_ListThreadsInSubCategoryPage_serializer(results, many=True)
    return self.get_paginated_response(data=serializer.data)


class Thread_Commenting_ApiView(CreateAPIView):
  permission_classes = [IsAuthenticated]
  serializer_class = ThreadPost_Serializer

  lookup_field = 'pk'
  lookup_url_kwarg = 'thread_id'

  def get_serializer_context(self):
    context = super(Thread_Commenting_ApiView, self).get_serializer_context()
    context.update({"request": self.request, 'kwargs': self.kwargs})
    return context


class Thread_LatestList_ApiView(ListAPIView):
  queryset = Thread.objects.all()
  serializer_class = Thread_LatestList_Serializer
  permission_classes = [AllowAny]
