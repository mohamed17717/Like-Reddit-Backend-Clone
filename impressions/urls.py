from django.urls import path
from rest_framework import routers
from .views import (
  Emoji_ApiView,

  PostEmoji_UserReact_ApiView,
  PostUpVote_UserReact_ApiView,
  PostDownVote_UserReact_ApiView
)

app_name = 'impressions'
router = routers.SimpleRouter()

router.register(r'emoji', Emoji_ApiView)

urlpatterns = [
  path('i/<int:post_id>/emoji/<int:emoji_id>/', PostEmoji_UserReact_ApiView.as_view(), name='user-react-emoji-to-post'),
  path('i/<int:post_id>/up/', PostUpVote_UserReact_ApiView.as_view(), name='user-react-upvote-to-post'),
  path('i/<int:post_id>/down/', PostDownVote_UserReact_ApiView.as_view(), name='user-react-downvote-to-post'),
] + router.urls




