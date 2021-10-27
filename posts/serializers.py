from rest_framework import serializers
from posts.models import PostConetntType, PostContent, PostState, Post, PostReplay


class PostConetntTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostConetntType
    fields = '__all__'


class PostContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostContent
    fields = '__all__'


class PostStateSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostState
    fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'


class PostReplaySerializer(serializers.ModelSerializer):
  class Meta:
    model = PostReplay
    fields = '__all__'

