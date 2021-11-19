from django.shortcuts import get_object_or_404
from rest_framework import serializers
from categories.models import SubCategory
from categories.serializers import SubCategory_ListFromThread_Serializer
from posts.models import Post, PostConetntType, PostContent
from posts.serializers import Post_Commenting_Serializer, Post_ForListing_Serializer, Post_InOwnerThreadActions_Serializer
from threads.models import ThreadState, Thread, ThreadPost, ThreadPin, ThreadDefaultSetting, ThreadUserVisit, Flair, ThreadFlair

def dict_get(d, *k):
    for i in k:
        yield d[i]

class ThreadStateSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadState
    fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thread
    fields = '__all__'


class Thread_Owner_serializer(serializers.ModelSerializer):
  post = Post_InOwnerThreadActions_Serializer()
  category = SubCategory_ListFromThread_Serializer() # serializers.CharField(source='category.name')
  state = serializers.CharField(source='state.state', read_only=True)
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
  state = serializers.CharField(source='state.state', read_only=True)

  url = serializers.URLField(source='get_absolute_url')
  class Meta:
    model = Thread
    fields = ('id', 'title', 'post', 'state', 'created', 'url', 'description')


class Thread_AdminUpdateState_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Thread
    fields = ('id', 'state',)

  def update(self, instance, validated_data):
    new_state = validated_data.get('state', instance.state)
    instance.state = new_state
    instance.save()
    return instance



class ThreadPost_Serializer(serializers.ModelSerializer):
  thread = ThreadSerializer(read_only=True)
  post = Post_Commenting_Serializer()
  # post = PostContentSerializer()
  class Meta:
    model = ThreadPost
    fields = ('post', 'thread')

  def create(self, validated_data):
    request, kwargs = dict_get(self.context, 'request', 'kwargs')

    user = request.user
    thread_id = kwargs.get('thread_id')
    thread = get_object_or_404(Thread, id=thread_id)
    post_data = validated_data.get('post')

    obj = Post.objects.create_comment_on_thread(user, thread, post_data)
    return obj


class ThreadPinSerializer(serializers.ModelSerializer):
  url = serializers.URLField(source='thread.get_absolute_url')
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

