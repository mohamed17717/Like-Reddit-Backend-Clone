from rest_framework import serializers
from follows.models import UserFollow, ThreadFollow


class UserFollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserFollow
    fields = '__all__'


class ThreadFollowSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadFollow
    fields = '__all__'

