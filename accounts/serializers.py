from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from accounts.models import UserVerified, UserPremium, UserBan
from follows.models import UserFollow


User = get_user_model()


# ------------- Djoser ------------- #
class UserCreateSerializer(UserCreateSerializer):
  class Meta(UserCreateSerializer.Meta):
    model = User
    fields = ('id', 'email', 'username', 'password')

    REQUIRED_FIELDS = ['username']


# ------------- Basic User Info ------------- #
class UserBasicPublicSerializer(serializers.ModelSerializer):
  profile_picture = serializers.StringRelatedField(source='profile.profile_picture.url')
  profile_url = serializers.StringRelatedField(source='profile.get_absolute_url')
  class Meta:
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture', 'profile_url')



# ------------- Profile Page ------------- #

class UserProfilePageSerializer(UserBasicPublicSerializer):
  is_followed = serializers.SerializerMethodField(read_only=True)
  is_own_profile = serializers.SerializerMethodField(read_only=True)
  followers_count = serializers.IntegerField(source='user_followers.count')
  following_count = serializers.IntegerField(source='user_targets.count')
  following_list_url = serializers.SerializerMethodField(read_only=True)
  followers_list_url = serializers.SerializerMethodField(read_only=True)

  class Meta(UserBasicPublicSerializer.Meta):
    fields = UserBasicPublicSerializer.Meta.fields + (
      'is_followed', 'is_own_profile',
      'following_count', 'followers_count',
      'following_list_url', 'followers_list_url'
    )

  def get_is_followed(self, obj):
    request = self.context['request']

    follow_state = False
    if request.user.is_authenticated:
      follow_state = UserFollow.objects.filter(target=obj, follower=request.user).exists()

    return follow_state

  def get_is_own_profile(self, obj):
    request = self.context['request']
    return request.user.is_authenticated and request.user.pk == obj.pk

  def get_following_list_url(self, obj):
    return reverse('follows:user-following-list', kwargs={'username': obj.username})

  def get_followers_list_url(self, obj):
    return reverse('follows:user-followers-list', kwargs={'username': obj.username})



# ------------- Verify Premium Ban ------------- #
class Abstract_User_VerifyPremiumBan_Serializer(serializers.ModelSerializer):
  user = UserBasicPublicSerializer(read_only=True)
  delete_url = serializers.SerializerMethodField()

  delete_url_viewname = None # required

  class Meta:
    model = None # required
    fields = ('user', 'delete_url')

  def get_delete_url(self, obj):
    return reverse(self.delete_url_viewname, kwargs={'pk': obj.pk})


class UserVerifiedSerializer(Abstract_User_VerifyPremiumBan_Serializer):
  delete_url_viewname = 'accounts:user-verify-detail'
  class Meta(Abstract_User_VerifyPremiumBan_Serializer.Meta):
    model = UserVerified

class UserPremiumSerializer(Abstract_User_VerifyPremiumBan_Serializer):
  delete_url_viename = 'accounts:user-premium-detail'
  class Meta(Abstract_User_VerifyPremiumBan_Serializer.Meta):
    model = UserPremium

class UserBanSerializer(Abstract_User_VerifyPremiumBan_Serializer):
  delete_url_viewname = 'accounts:user-ban-detail'
  class Meta(Abstract_User_VerifyPremiumBan_Serializer.Meta):
    model = UserBan

