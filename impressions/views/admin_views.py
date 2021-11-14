from core.generics import CreateDestroyListViewSet
from core.permissions import IsAdminOrReadOnly

from impressions.models import Emoji
from impressions.serializers import EmojiSerializer

class Emoji_ApiView(CreateDestroyListViewSet):
  queryset = Emoji.objects.all()
  serializer_class = EmojiSerializer
  permission_classes = [IsAdminOrReadOnly]

