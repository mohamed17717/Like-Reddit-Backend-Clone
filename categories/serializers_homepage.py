from rest_framework import serializers

from threads.serializers import Thread_BasicInfo_Serializer
from categories.serializers import SubCategoryBasicSerializer, CategoryBasicSerializer


class SubCategory_Homepage_Serializer(SubCategoryBasicSerializer):
  threads_count = serializers.IntegerField(source='threads.count', read_only=True)
  latest_thread = Thread_BasicInfo_Serializer(source='threads.first')
  class Meta(SubCategoryBasicSerializer.Meta):
    fields = SubCategoryBasicSerializer.Meta.fields + ('threads_count', 'latest_thread')

class Category_Homepage_Serializer(CategoryBasicSerializer):
  sub_categories = SubCategory_Homepage_Serializer(many=True, read_only=True)
  class Meta(CategoryBasicSerializer.Meta):
    fields = CategoryBasicSerializer.Meta.fields + ('sub_categories',)


