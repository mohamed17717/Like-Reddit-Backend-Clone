from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_401_UNAUTHORIZED

from accounts.serializers import UserBasicPublicSerializer


User = get_user_model()

class Abstract_UserFollow_ApiView(APIView, LimitOffsetPagination):
  permission_classes = [AllowAny]
  count = 20

  def get_user(self, request, username):
    user = None
    if username != None:
      user = get_object_or_404(User, username=username)
    elif request.user.is_authenticated:
      user = request.user
    else:
      raise APIException(code=HTTP_401_UNAUTHORIZED)
    
    return user

  # required
  def get_queryset(self, request, username):
    ...
  
  def get(self, request, username=None):
    qs = self.get_queryset(request, username)

    results = self.paginate_queryset(qs, request, view=self)
    serializer = UserBasicPublicSerializer(results, many=True)

    return self.get_paginated_response(data=serializer.data)



class UserFollowingList_ApiView(Abstract_UserFollow_ApiView):
  def get_queryset(self, request, username):
    user = self.get_user(request, username)
    qs = User.objects.filter(user_followers__follower=user)

    return qs

class UserFollowersList_ApiView(Abstract_UserFollow_ApiView):
  def get_queryset(self, request, username):
    user = self.get_user(request, username)
    qs = User.objects.filter(user_targets__target=user)

    return qs


