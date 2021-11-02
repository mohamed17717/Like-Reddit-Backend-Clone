from rest_framework import serializers
from categories.models import Category, SubCategory

class CategoryBasicSerializer(serializers.ModelSerializer):
  class Meta:
    model = SubCategory
    fields = ['name', 'id']

class SubCategoryBasicSerializer(serializers.ModelSerializer):
  threads_count = serializers.IntegerField(source='threads.count', read_only=True)
  class Meta:
    model = SubCategory
    fields = ['name', 'id', 'threads_count']


# ------------------- full ----------------- #
class CategorySerializer(serializers.ModelSerializer):
  sub_categories = SubCategoryBasicSerializer(many=True, read_only=True)
  class Meta:
    model = Category
    fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
  category = CategoryBasicSerializer(read_only=True)
  threads_count = serializers.IntegerField(source='threads.count', read_only=True)
  class Meta:
    model = SubCategory
    fields = '__all__'

