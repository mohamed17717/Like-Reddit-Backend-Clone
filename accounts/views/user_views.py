from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers import UserBasicPublicSerializer
from follows.models import UserFollow


User = get_user_model()

class UserProfile_ApiView(APIView):
  def get(self, request, username):
    user = get_object_or_404(User, username=username)
    serialized = UserBasicPublicSerializer(user)

    check_follow = False
    if request.user.is_authenticated:
      check_follow = UserFollow.objects.filter(target=user, follower=request.user).exists()

    data = {**serialized.data, 'is_followed': check_follow}
    return Response(data)


