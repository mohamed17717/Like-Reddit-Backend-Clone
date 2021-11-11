from django.contrib.auth import get_user_model
from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from accounts.models import UserProfile, UserVerified, UserPremium, UserBan


User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer.Meta):
    model = User
    fields = ('id', 'email', 'username', 'password')
    
    REQUIRED_FIELDS = ['username']



class UserBasicPublicSerializer(serializers.ModelSerializer):
  profile_picture = serializers.StringRelatedField(source='profile.profile_picture.url')
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture',)

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserProfile
    fields = '__all__'


class UserVerifiedSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserVerified
    fields = '__all__'


class UserPremiumSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserPremium
    fields = '__all__'


class UserBanSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserBan
    fields = '__all__'

