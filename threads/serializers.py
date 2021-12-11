from django.shortcuts import get_object_or_404

from rest_framework import serializers
from accounts.serializers import UserBasicPublicSerializer

from categories.models import SubCategory
from posts.models import Post
from threads.models import Thread
from states.models import PendingState

from categories.serializers import SubCategory_PlusParent_Serializer
from posts.serializers import PostSerializer



class Thread_BasicInfo_Serializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(source='post.user',read_only=True)
  url = serializers.CharField(source='get_absolute_url')
  category = SubCategory_PlusParent_Serializer()

  class Meta:
    model = Thread
    fields = (
      'user', 'url', 'title', 'description', 'category',
      'is_private', 'created', 'visits_count', 'comments_count'
    )

class Thread_HandlePendingState_Serializer(Thread_BasicInfo_Serializer):
  class Meta(Thread_BasicInfo_Serializer.Meta):
    model = Thread
    fields = Thread_BasicInfo_Serializer.Meta.fields + ('pending_state',)
    read_only_fields = Thread_BasicInfo_Serializer.Meta.fields

  def update(self, instance, validated_data):
    new_state_value = validated_data.get('pending_state', instance.state)
    new_state, _ = PendingState.objects.get_or_create(state=new_state_value)

    instance.pending_state = new_state
    instance.save()
    return instance


class Thread_FullInfo_Serializer(Thread_BasicInfo_Serializer):
  post = PostSerializer()
  comments = PostSerializer(source='posts', many=True, allow_null=True)
  class Meta(Thread_BasicInfo_Serializer.Meta):
    fields = Thread_BasicInfo_Serializer.Meta.fields + ('post', 'comments')


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




