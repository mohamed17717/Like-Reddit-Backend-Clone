from rest_framework import serializers
from threads.models import ThreadStates, Thread, ThreadPost, ThreadPin, ThreadDefaultSetting, ThreadUserVisit, Flair, ThreadFlair


class ThreadStatesSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadStates
    fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
  class Meta:
    model = Thread
    fields = '__all__'


class ThreadPostSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadPost
    fields = '__all__'


class ThreadPinSerializer(serializers.ModelSerializer):
  class Meta:
    model = ThreadPin
    fields = '__all__'


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

