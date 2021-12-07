from django.shortcuts import get_object_or_404

from rest_framework import serializers

from categories.models import SubCategory
from posts.models import Post
from threads.models import Thread, ThreadPost, ThreadPin, ThreadDefaultSetting, ThreadUserVisit, Flair, ThreadFlair
from states.models import PendingState

from categories.serializers import SubCategory_PlusParent_Serializer
from posts.serializers import Post_Commenting_Serializer, Post_ForListing_Serializer, Post_InOwnerThreadActions_Serializer


def dict_get(d, *k):
  for i in k:
    yield d[i]


class ThreadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thread
    fields = '__all__'


class Thread_Owner_serializer(serializers.ModelSerializer):
  post = Post_InOwnerThreadActions_Serializer()
  category = SubCategory_PlusParent_Serializer()
  state = serializers.CharField(source='privacy_state.state', read_only=True)
  class Meta:
    model = Thread
    fields = ('id', 'title', 'post', 'state', 'category', 'created')

  def create(self, validated_data):
    request = self.context.get('request')
    post_data = validated_data.get('post')
    post = Post.objects.create_deep({'user': request.user, **post_data})

    category_data = validated_data.get('category')
    category = get_object_or_404(SubCategory, **category_data)

    validated_data.update({'post': post, 'category': category})
    return Thread.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)

    category_data = validated_data.get('category', {'name': instance.category.name})
    instance.category = get_object_or_404(SubCategory, **category_data)

    post_data = validated_data.get('post')
    Post.objects.update_deep(instance.post, post_data)

    instance.category.save()
    instance.save()

    return instance



class Thread_ListThreadsInSubCategoryPage_serializer(serializers.ModelSerializer):
  post = Post_ForListing_Serializer(read_only=True)
  url = serializers.URLField(source='get_absolute_url', read_only=True)
  class Meta:
    model = Thread
    fields = ('id', 'title', 'post', 'created', 'url', 'description')


class Thread_LatestList_Serializer(serializers.ModelSerializer):
  post = Post_ForListing_Serializer(read_only=True)
  url = serializers.URLField(source='get_absolute_url', read_only=True)
  category = serializers.CharField(source='category.name', read_only=True)
  class Meta:
    model = Thread
    fields = ('id', 'is_private', 'title', 'post', 'created', 'url', 'description', 'category')

class Thread_AdminUpdatePendingState_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Thread
    fields = ('id', 'pending_state',)

  def update(self, instance, validated_data):
    new_state_value = validated_data.get('pending_state', instance.state)
    new_state, _ = PendingState.objects.get_or_create(state=new_state_value)

    instance.pending_state = new_state
    instance.save()
    return instance

class Thread_ListAsPending_Serializer(serializers.ModelSerializer):
  url = serializers.URLField(source='get_absolute_url', read_only=True)
  category = serializers.CharField(source='category.name', read_only=True)

  class Meta:
    model = Thread
    fields = ('id', 'pending_state', 'url', 'title', 'description', 'category', 'created')

class ThreadPost_Serializer(serializers.ModelSerializer):
  thread = ThreadSerializer(read_only=True)
  post = Post_Commenting_Serializer()

  class Meta:
    model = ThreadPost
    fields = ('post', 'thread')

  def create(self, validated_data):
    request, kwargs = dict_get(self.context, 'request', 'kwargs')

    thread = Thread.objects.one_alive(pk=kwargs.get('thread_id'))
    post_data = validated_data.get('post')

    obj = Post.objects.create_comment_on_thread(request.user, thread, post_data)
    return obj


class ThreadPinSerializer(serializers.ModelSerializer):
  # url = serializers.URLField(source='thread.get_absolute_url')
  thread = Thread_LatestList_Serializer(read_only=True)
  class Meta:
    model = ThreadPin
    fields = ('thread', 'url')


class ThreadDefaultSettingSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadDefaultSetting
    fields = '__all__'


class ThreadUserVisitSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadUserVisit
    fields = '__all__'


class FlairSerializer(serializers.ModelSerializer):
  class Meta:
    model = Flair
    fields = '__all__'


class ThreadFlairSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadFlair
    fields = '__all__'

