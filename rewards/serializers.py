from rest_framework import serializers

from accounts.serializers import UserBasicPublicSerializer
from rewards.models import UserKarma


class UserKarmaSerializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(read_only=True)
  class Meta:
    model = UserKarma
    fields = '__all__'

