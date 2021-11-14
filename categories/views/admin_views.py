from rest_framework.permissions import IsAdminUser

from core.generics import CreateUpdateDestroyListViewSet

from categories.models import Category, SubCategory
from categories.serializers import CategorySerializer, SubCategorySerializer


class Category_ApiView(CreateUpdateDestroyListViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  permission_classes = [IsAdminUser]


class SubCategory_ApiView(CreateUpdateDestroyListViewSet):
  queryset = SubCategory.objects.all()
  serializer_class = SubCategorySerializer
  permission_classes = [IsAdminUser]

