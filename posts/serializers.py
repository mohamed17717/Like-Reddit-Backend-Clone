from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from accounts.serializers import UserBasicPublicSerializer
from posts.models import PostConetntType, PostContent, PostState, Post, PostReplay



class PostContentSerializer(serializers.ModelSerializer):
  type = serializers.CharField(source='type.type')
  class Meta:
    model = PostContent
    fields = ('type', 'content')

  def clean_type(self):
    allowed_types = ['text', 'html', 'markdown']
    type = self.cleaned_data.get('type')
    if type not in allowed_types:
      raise serializers.ValidationError(f'type {type} is not, Allowed types are [{", ".join(allowed_types)}] ')
    return type


class PostStateSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostState
    fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

class Post_InOwnerThreadActions_Serializer(serializers.ModelSerializer):
  post_content = PostContentSerializer()

  class Meta:
    model = Post
    fields = ('description', 'post_content', )


class Post_Commenting_Serializer(serializers.ModelSerializer):
  post_content = PostContentSerializer()

  class Meta:
    model = Post
    fields = ('post_content', 'id')

class Post_ForListing_Serializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(read_only=True)
  class Meta:
    model = Post
    fields = ('id', 'description', 'user',)


class Post_OwnerActions_Serializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(read_only=True)
  # post_content = PostContentSerializer()
  comment = serializers.CharField(source='post_content.content')
  comment_type = serializers.CharField(source='post_content.type')
  state = serializers.CharField(source='state.name', read_only=True)

  class Meta:
    model = Post
    fields = ('id','user', 'comment', 'comment_type', 'state')

  def update(self, instance, validated_data):
    post = Post.objects.update_deep(instance, validated_data)
    return post

  def create(self, validated_data):
    request = self.context.get('request')
    kwargs = self.context.get('kwargs')

    post_id = kwargs.get('post_id')

    replay = Post.objects.create_replay_on_comment(request.user, post_id, validated_data)
    return replay

class Post_UpdateState_serializer(serializers.ModelSerializer):
  state = serializers.CharField(source='state.name')
  class Meta:
    model = Post
    fields = ('id', 'state')

  def update(self, instance, validated_data):
    obj = Post.objects.update_deep(instance, validated_data)
    return obj


class PostReplaySerializer(serializers.ModelSerializer):
  # post = Post_OwnerActions_Serializer(read_only=True)
  replay = Post_OwnerActions_Serializer(read_only=True)
  class Meta:
    model = PostReplay
    fields = ('id', 'replay', )

