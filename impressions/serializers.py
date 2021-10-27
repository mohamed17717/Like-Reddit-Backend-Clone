from rest_framework import serializers
from impressions.models import Emoji, PostEmoji, PostUpVote, PostDownVote


class EmojiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Emoji
    fields = '__all__'


class PostEmojiSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostEmoji
    fields = '__all__'


class PostUpVoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostUpVote
    fields = '__all__'


class PostDownVoteSerializer(serializers.ModelSerializer):
  class Meta:
    model = PostDownVote
    fields = '__all__'

