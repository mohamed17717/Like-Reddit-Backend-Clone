from rest_framework import serializers
from categories.models import Category, SubCategory

from threads.t_serializers.thread import ThreadSerializer


# ------------ Basic ------------ #
class CategoryBasicSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='get_absolute_url')
  class Meta:
    model = Category
    fields = ('name', 'is_private', 'url')

class SubCategoryBasicSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='get_absolute_url')
  class Meta:
    model = SubCategory
    fields = ('name',  'is_private', 'url')

class SubCategory_PlusParent_Serializer(SubCategoryBasicSerializer):
  category = CategoryBasicSerializer(read_only=True)
  class Meta(SubCategoryBasicSerializer.Meta):
    fields = SubCategoryBasicSerializer.Meta.fields + ('category',)


# ------------ Homepage++ ------------ #
class SubCategory_Homepage_Serializer(SubCategoryBasicSerializer):
  threads_count = serializers.IntegerField(source='threads.count', read_only=True)
  latest_thread = ThreadSerializer(source='threads.first')
  class Meta(SubCategoryBasicSerializer.Meta):
    fields = SubCategoryBasicSerializer.Meta.fields + ('threads_count', 'latest_thread')

class Category_Homepage_Serializer(CategoryBasicSerializer):
  sub_categories = SubCategory_Homepage_Serializer(many=True, read_only=True)
  class Meta(CategoryBasicSerializer.Meta):
    fields = CategoryBasicSerializer.Meta.fields + ('sub_categories',)


