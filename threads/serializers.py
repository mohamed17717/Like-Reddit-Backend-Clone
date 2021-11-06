from django.shortcuts import get_object_or_404
from rest_framework import serializers
from categories.models import SubCategory
from categories.serializers import SubCategory_ListFromThread_Serializer
from posts.models import Post, PostConetntType, PostContent
from posts.serializers import Post_Commenting_Serializer, Post_ForListing_Serializer, Post_InOwnerThreadActions_Serializer
from threads.models import ThreadState, Thread, ThreadPost, ThreadPin, ThreadDefaultSetting, ThreadUserVisit, Flair, ThreadFlair


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
    category_data = validated_data.get('category')

    category = get_object_or_404(SubCategory, **category_data)
    validated_data['category'] = category

    post_data = validated_data.get('post')
    post_content_data = post_data.get('post_content')
    post_content_type_data = post_content_data.get('type')

    post_content_data['type'], _ = PostConetntType.objects.get_or_create(**post_content_type_data)
    post_data['post_content'] = PostContent.objects.create(**post_content_data)
    post_data['user'] = self.context.get('request').user
    validated_data['post'] = Post.objects.create(**post_data)
    
    instance = Thread.objects.create(**validated_data)
    return instance

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)

    category_data = validated_data.get('category', {'name': instance.category.name})
    instance.category = get_object_or_404(SubCategory, **category_data)

    post_data = validated_data.get('post')
    instance.post.description = post_data.get('description', instance.post.description)

    post_content_data = post_data.get('post_content')
    instance.post.post_content.content = post_content_data.get('content', instance.post.post_content.content)
    post_content_type_data = post_content_data.get('type', {'type': instance.post.post_content.type.type})
    instance.post.post_content.type, _ = PostConetntType.objects.get_or_create(**post_content_type_data)
    
    instance.category.save()
    instance.post.save()
    instance.post.post_content.save()
    instance.save()

    return instance


    return 




class Thread_ListThreadsInSubCategoryPage_serializer(serializers.ModelSerializer):
  post = Post_ForListing_Serializer(read_only=True)
  state = serializers.CharField(source='state.state', read_only=True)

  url = serializers.URLField(source='get_absolute_url')
  class Meta:
    model = Thread
    fields = ('id', 'title', 'post', 'state', 'created', 'url')


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
    thread_id = self.context.get('kwargs')['pk']
    thread = get_object_or_404(Thread, id=thread_id)

    post = validated_data.get('post').get('post_content')

    content_data = post.get('content')
    type_data = post.get('type')
    type, _ = PostConetntType.objects.get_or_create(**type_data)

    post_content = PostContent.objects.create(content=content_data, type=type)

    post = Post.objects.create(user=self.context.get('request').user, post_content=post_content)

    print('\n\nPOST: ', post)
    instance = ThreadPost.objects.create(post=post, thread=thread)
    print('instance: ',instance, '\n\n')
    return instance


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

