from categories.models import Category, SubCategory
from categories.serializers import CategorySerializer, SubCategorySerializer

from core.generics import CreateUpdateDestroyListViewSet
from core.permissions import IsAdminOrReadOnly


class Category_ApiView(CreateUpdateDestroyListViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer

  permission_classes = [IsAdminOrReadOnly]


class SubCategory_ApiView(CreateUpdateDestroyListViewSet):
  queryset = SubCategory.objects.all()
  serializer_class = SubCategorySerializer

  permission_classes = [IsAdminOrReadOnly]

