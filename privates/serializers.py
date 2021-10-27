from rest_framework import serializers
from privates.models import PrivateContent


class PrivateContentSerializer(serializers.ModelSerializer):
  class Meta:
    model = PrivateContent
    fields = '__all__'

