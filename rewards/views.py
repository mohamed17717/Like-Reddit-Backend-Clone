from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAdminUser

from rewards.models import UserKarma
from rewards.serializers import UserKarmaSerializer


class UserKarma_List_ApiView(APIView, LimitOffsetPagination):
  permission_classes = [IsAdminUser]

  def get(self, request, **kwargs):
    qs = UserKarma.objects.all()
    results = self.paginate_queryset(qs, request, view=self)
    serialized = UserKarmaSerializer(results, many=True)

    return self.get_paginated_response(serialized.data)
