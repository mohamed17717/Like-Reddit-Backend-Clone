from rest_framework.permissions import IsAdminUser

from core.generics import CreateUpdateDestroyListViewSet

from impressions.models import Emoji
from impressions.serializers import EmojiSerializer

class Emoji_ApiView(CreateUpdateDestroyListViewSet):
  queryset = Emoji.objects.all()
  serializer_class = EmojiSerializer
  permission_classes = [IsAdminUser]
