from rest_framework import serializers
from rewards.models import UserKarma


class UserKarmaSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserKarma
    fields = '__all__'

