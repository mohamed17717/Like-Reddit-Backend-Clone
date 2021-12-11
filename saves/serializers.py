from rest_framework import serializers
from saves.models import SavePost

from posts.serializers import Post_ToThreadRelation_Serializer

class SavePostSerializer(serializers.ModelSerializer):
  post = Post_ToThreadRelation_Serializer(read_only=True)
  class Meta:
    model = SavePost
    fields = ('post',)

