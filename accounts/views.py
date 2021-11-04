from rest_framework.permissions import IsAdminUser

from core.generics import CreateDestroyListViewSet

from accounts.models import UserBan, UserPremium, UserVerified
from accounts.serializers import UserBanSerializer, UserPremiumSerializer, UserVerifiedSerializer

class UserVerified_ApiView(CreateDestroyListViewSet):
  queryset = UserVerified.objects.all()
  serializer_class = UserVerifiedSerializer
  permission_classes = [IsAdminUser]

class UserPremium_ApiView(CreateDestroyListViewSet):
  queryset = UserPremium.objects.all()
  serializer_class = UserPremiumSerializer
  permission_classes = [IsAdminUser]

class UserBan_ApiView(CreateDestroyListViewSet):
  queryset = UserBan.objects.all()
  serializer_class = UserBanSerializer
  permission_classes = [IsAdminUser]

