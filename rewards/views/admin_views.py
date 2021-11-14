from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from rewards.models import UserKarma
from rewards.serializers import UserKarmaSerializer


class UserKarma_List_ApiView(ListAPIView):
  queryset = UserKarma.objects.all()
  permission_classes = [IsAdminUser]
  serializer_class = UserKarmaSerializer
