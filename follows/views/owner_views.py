from django.contrib.auth import get_user_model

from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.serializers import UserBasicPublicSerializer


User = get_user_model()



class UserFollow_ListFollows_ApiView(views.APIView):
  ''' People he has follows '''
  permission_classes = [IsAuthenticated]

  def get(self, request, **kwargs):
    qs = User.objects.filter(user_followers__follower=request.user)
    serialized = UserBasicPublicSerializer(qs, many=True)

    return Response(serialized.data)

class UserFollow_ListFollowers_ApiView(views.APIView):
  ''' People follows him '''
  permission_classes = [IsAuthenticated]

  def get(self, request, **kwargs):
    qs = User.objects.filter(user_targets__target=request.user)
    serialized = UserBasicPublicSerializer(qs, many=True)

    return Response(serialized.data)


