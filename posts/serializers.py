from django.urls import reverse

from rest_framework import serializers

from accounts.serializers import UserBasicPublicSerializer
from posts.models import Post


class Post_ToThreadRelation_Serializer(serializers.ModelSerializer):
  url = serializers.CharField(source='get_absolute_url')
  thread_title = serializers.CharField(source='get_thread_title')
  thread_relation = serializers.CharField(source='get_thread_relation')
  class Meta:
    model = Post
    fields = ('url', 'thread_title', 'thread_relation')

class PostSerializer(serializers.ModelSerializer):
  url = serializers.CharField(source='get_absolute_url', read_only=True)
  urls = serializers.SerializerMethodField(read_only=True)
  user = UserBasicPublicSerializer(read_only=True)

  content = serializers.CharField(source="post_content.content")
  content_type = serializers.CharField(source="post_content.type.type")

  class Meta:
    model = Post
    fields = (
      'user', 'content', 'content_type', 'created', 'upvote_count',
      'downvote_count', 'emoji_count', 'replays_count',
      'url', 'urls'
    )
    extra_kwargs = {
      'created': {'read_only': True},
      'upvote_count': {'read_only': True},
      'downvote_count': {'read_only': True},
      'emoji_count': {'read_only': True},
      'replays_count': {'read_only': True},
    }

  def get_urls(self, obj):
    return {
      'save_url': reverse('saves:save-post-toggle', kwargs={'post_id': obj.pk}), 
      'upvote_url': reverse('impressions:user-react-upvote-to-post', kwargs={'post_id': obj.pk}), 
      'downvote_url': reverse('impressions:user-react-downvote-to-post', kwargs={'post_id': obj.pk}), 
      'replay_url': reverse('posts:create-post-replay', kwargs={'post_id': obj.pk}),
      'list_replays_url': reverse('posts:list-post-replays', kwargs={'post_id': obj.pk}),
    }

  def update(self, instance, validated_data):
    post = Post.objects.update_deep(instance, validated_data)
    return post

  def create(self, validated_data):
    context = self.context

    user = context['request'].user
    validated_data.update({'user': user})

    post = Post.objects.create_deep(validated_data)

    create_method = {
      'replay': Post.objects.create_replay_on_comment,
      'comment': Post.objects.create_comment_on_thread,
      'thread_post': None # already created
    }.get(context.get('post_type'))

    if create_method:
      create_method(post, context['to'])

    return post

