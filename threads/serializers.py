from django.shortcuts import get_object_or_404

from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_400_BAD_REQUEST

from accounts.serializers import UserBasicPublicSerializer

from categories.models import SubCategory
from posts.models import Post
from threads.models import Thread
from states.models import PendingState

from categories.serializers import SubCategory_PlusParent_Serializer
from posts.serializers import PostSerializer



class Thread_BasicInfo_Serializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(source='post.user', read_only=True)
  url = serializers.CharField(source='get_absolute_url', read_only=True)
  sub_category = SubCategory_PlusParent_Serializer(source="category", read_only=True)
  sub_category_id = serializers.IntegerField(write_only=True)

  class Meta:
    model = Thread
    fields = (
      'user', 'url', 'title', 'description', 'sub_category', 'sub_category_id',
      'is_private', 'created', 'visits_count', 'comments_count',
    )

    extra_kwargs = {
      'is_private': {'read_only': True},
      'created': {'read_only': True},
      'visits_count': {'read_only': True},
      'comments_count': {'read_only': True},
    }

class Thread_ReadPendingState_Serializer(Thread_BasicInfo_Serializer):
  pending_state = serializers.CharField(source='pending_state.state')
  class Meta(Thread_BasicInfo_Serializer.Meta):
    model = Thread
    fields = Thread_BasicInfo_Serializer.Meta.fields + ('pending_state',)
    read_only_fields = Thread_BasicInfo_Serializer.Meta.fields


class Thread_WritePendingState_Serializer(serializers.ModelSerializer):
  pending_state = serializers.CharField(source='pending_state.state')
  class Meta:
    model = Thread
    fields = ('pending_state',)

  def validate_pending_state(self, value):
    if value not in PendingState.states:
      raise APIException(detail=f'only allowed {", ".join(PendingState.states)}', code=HTTP_400_BAD_REQUEST)
    return value

  def update(self, instance, validated_data):
    new_state_value = validated_data.get('pending_state', instance.pending_state.state)
    new_state, _ = PendingState.objects.get_or_create(state=new_state_value)

    instance.pending_state = new_state
    instance.save()

    return instance


class Thread_FullInfo_Serializer(Thread_BasicInfo_Serializer):
  post = PostSerializer()
  comments = PostSerializer(source='posts', many=True, allow_null=True, read_only=True)
  class Meta(Thread_BasicInfo_Serializer.Meta):
    fields = Thread_BasicInfo_Serializer.Meta.fields + ('post', 'comments')


  def create(self, validated_data):
    request = self.context.get('request')

    post_data = validated_data.get('post')
    post = Post.objects.create_deep({'user': request.user, **post_data})

    category_id = validated_data.pop('sub_category_id')
    category = get_object_or_404(SubCategory, pk=category_id)

    validated_data.update({'post': post, 'category': category})

    return Thread.objects.create(**validated_data)

  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)

    category_id = validated_data.get('sub_category_id', instance.category.pk)
    instance.category = get_object_or_404(SubCategory, pk=category_id)

    post_data = validated_data.get('post')
    Post.objects.update_deep(instance.post, post_data)

    instance.category.save()
    instance.save()

    return instance


class Thread_Owner_Serializer(Thread_FullInfo_Serializer):
  pending_state = serializers.CharField(source='pending_state.state', read_only=True)
  privacy_state = serializers.CharField(source='privacy_state.state', read_only=True)
  class Meta(Thread_FullInfo_Serializer.Meta):
    fields = Thread_FullInfo_Serializer.Meta.fields + ('pending_state', 'privacy_state')


