from rest_framework.permissions import IsAdminUser

from core.generics import CreateUpdateDestroyListViewSet

from categories.models import Category, SubCategory
from categories.serializers import CategoryBasicSerializer, SubCategory_PlusParent_Serializer


class Category_ApiView(CreateUpdateDestroyListViewSet):
  queryset = Category.objects.all()
  serializer_class = CategoryBasicSerializer
  permission_classes = [IsAdminUser]


class SubCategory_ApiView(CreateUpdateDestroyListViewSet):
  queryset = SubCategory.objects.all()
  serializer_class = SubCategory_PlusParent_Serializer
  permission_classes = [IsAdminUser]

