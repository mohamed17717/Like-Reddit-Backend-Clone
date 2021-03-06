from rest_framework import serializers
from categories.models import Category, SubCategory


class CategoryBasicSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='get_absolute_url', read_only=True)
  class Meta:
    model = Category
    fields = ('name', 'is_private', 'url')

class SubCategoryBasicSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='get_absolute_url', read_only=True)
  class Meta:
    model = SubCategory
    fields = ('name',  'is_private', 'url')

class SubCategory_PlusParent_Serializer(SubCategoryBasicSerializer):
  category = CategoryBasicSerializer(read_only=True)
  category_id = serializers.IntegerField(write_only=True)
  class Meta(SubCategoryBasicSerializer.Meta):
    fields = SubCategoryBasicSerializer.Meta.fields + ('category', 'category_id')

