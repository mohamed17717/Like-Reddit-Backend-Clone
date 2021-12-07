from django.contrib.auth import get_user_model

from rest_framework import views
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from accounts.serializers import UserBasicPublicSerializer


User = get_user_model()



class UserFollow_ListFollows_ApiView(views.APIView, LimitOffsetPagination):
  ''' People he has follows '''
  permission_classes = [IsAuthenticated]

  def get(self, request, **kwargs):
    qs = User.objects.filter(user_followers__follower=request.user)

    results = self.paginate_queryset(qs, request, view=self)
    serializer = UserBasicPublicSerializer(results, many=True)

    return self.get_paginated_response(data=serializer.data)


class UserFollow_ListFollowers_ApiView(views.APIView, LimitOffsetPagination):
  ''' People follows him '''
  permission_classes = [IsAuthenticated]

  def get(self, request, **kwargs):
    qs = User.objects.filter(user_targets__target=request.user)

    results = self.paginate_queryset(qs, request, view=self)
    serializer = UserBasicPublicSerializer(results, many=True)

    return self.get_paginated_response(data=serializer.data)


