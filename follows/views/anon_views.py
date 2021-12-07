from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import views
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from accounts.serializers import UserBasicPublicSerializer


User = get_user_model()



class UserFollowingList_ApiView(views.APIView, LimitOffsetPagination):
  permission_classes = [AllowAny]

  def get(self, request, username):
    user = get_object_or_404(User, username=username)
    qs = User.objects.filter(user_followers__follower=user)

    results = self.paginate_queryset(qs, request, view=self)
    serializer = UserBasicPublicSerializer(results, many=True)

    return self.get_paginated_response(data=serializer.data)


class UserFollowersList_ApiView(views.APIView, LimitOffsetPagination):
  permission_classes = [AllowAny]

  def get(self, request, username):
    user = get_object_or_404(User, username=username)
    qs = User.objects.filter(user_targets__target=user)

    results = self.paginate_queryset(qs, request, view=self)
    serializer = UserBasicPublicSerializer(results, many=True)

    return self.get_paginated_response(data=serializer.data)


