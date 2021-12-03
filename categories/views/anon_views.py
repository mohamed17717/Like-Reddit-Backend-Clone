from django.shortcuts import get_object_or_404

from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from categories.models import Category
from categories.serializers import CategorySerializer, SubCategorySerializer

from core.permissions import IsUserHasAccess


class Category_UserList_ApiView(ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [AllowAny]

class SubCategory_ListOnCategory_ApiView(APIView, LimitOffsetPagination):
  serializer_class = SubCategorySerializer
  permission_classes = [AllowAny]
  count = 20

  def get(self, request, category_id):
    category = get_object_or_404(Category, pk=category_id)

    IsUserHasAccess(request, category)

    sub_categories = category.sub_categories.all()
    results = self.paginate_queryset(sub_categories, request, view=self)

    serialized = self.serializer_class(results, many=True)
    return self.get_paginated_response(data=serialized.data)

