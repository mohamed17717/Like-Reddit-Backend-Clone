from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from accounts.serializers import UserProfilePageSerializer


User = get_user_model()

class UserProfile_ApiView(APIView):
  permission_classes = [AllowAny]

  def get(self, request, username):
    user = get_object_or_404(User, username=username)
    serialized = UserProfilePageSerializer(user, context={'request': request})

    return Response(serialized.data)


