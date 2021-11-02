from rest_framework import serializers
from saves.models import SavePost

from posts.serializers import PostSerializer

class SavePostSerializer(serializers.ModelSerializer):
  post_thread_url = serializers.URLField(source='post.get_absolute_url')
  post = PostSerializer(read_only=True)
  class Meta:
    model = SavePost
    fields = ('post', 'post_thread_url')

