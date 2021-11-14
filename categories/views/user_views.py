from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from categories.models import Category, SubCategory
from categories.serializers import CategorySerializer, SubCategorySerializer


class Category_UserList_ApiView(ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [AllowAny]


class SubCategory_UserList_ApiView(ListAPIView):
  queryset = SubCategory.objects.all()
  serializer_class = SubCategorySerializer
  permission_classes = [AllowAny]

