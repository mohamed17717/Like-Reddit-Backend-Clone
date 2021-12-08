from rest_framework import serializers
from impressions.models import Emoji


class EmojiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Emoji
    fields = '__all__'

