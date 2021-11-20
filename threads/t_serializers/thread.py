from posts.serializers import Post_ForListing_Serializer
from threads.models import Thread
from rest_framework import serializers 

class ThreadSerializer(serializers.ModelSerializer):
  post = Post_ForListing_Serializer(read_only=True)
  url = serializers.CharField(source='get_absolute_url')
  class Meta:
    model = Thread
    fields = ('post', 'id', 'title', 'description', 'created', 'url')
