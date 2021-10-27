from rest_framework import serializers
from saves.models import SavePost


class SavePostSerializer(serializers.ModelSerializer):
  class Meta:
    model = SavePost
    fields = '__all__'

