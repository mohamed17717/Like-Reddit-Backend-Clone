from rest_framework import serializers
from accounts.models import UserProfile, UserVerified, UserPremium, UserBan


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

