from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.generics import get_object_or_404

from accounts.serializers import UserBasicPublicSerializer
from posts.models import PostConetntType, PostContent, PostState, Post, PostReplay


class PostConetntTypeSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostConetntType
    fields = '__all__'


class PostContentSerializer(serializers.ModelSerializer):
  type = serializers.CharField(source='type.type')
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


class Post_OwnerActions_Serializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(read_only=True)
  post_content = PostContentSerializer()
  class Meta:
    model = Post
    fields = ('id','user', 'post_content')

  def update(self, instance, validated_data):
    post_content_data = validated_data.pop('post_content')
    post_content = instance.post_content

    post_content_type_data = post_content_data.pop('type')
    post_content_type, _ = PostConetntType.objects.get_or_create(**post_content_type_data)

    post_content.content = post_content_data.get('content', post_content.content)
    post_content.type = post_content_type
    post_content.save()

    return instance

  def create(self, validated_data):
    request = self.context.get('request')
    
    kwargs = self.context.get('kwargs')
    post_id = kwargs.get('post_id')
    main_post = get_object_or_404(Post, id=post_id)

    post_content_data = validated_data.pop('post_content')
    post_content_type_data = post_content_data.pop('type')

    type, _ = PostConetntType.objects.get_or_create(**post_content_type_data)
    post_content = PostContent.objects.create(type=type, **post_content_data)

    replay = Post.objects.create(post_content=post_content, user=request.user)

    PostReplay.objects.create(post=main_post, replay=replay)
    return replay

class Post_UpdateState_serializer(serializers.ModelSerializer):
  state = serializers.CharField(source='state.name')
  class Meta:
    model = Post
    fields = ('id', 'state')

  def update(self, instance, validated_data):
    state_data = validated_data.pop('state')
    new_state, _ = PostState.objects.get_or_create(**state_data)

    instance.state = new_state
    instance.save()

    return instance


class PostReplaySerializer(serializers.ModelSerializer):
  # post = Post_OwnerActions_Serializer(read_only=True)
  replay = Post_OwnerActions_Serializer(read_only=True)
  class Meta:
    model = PostReplay
    fields = ('id', 'replay', )

