from django.urls import path
from rest_framework import routers

from impressions.views.admin_views import Emoji_ApiView
from impressions.views.user_views import (
  Emoji_UserList_ApiView,
  PostEmoji_UserReact_ApiView,
  PostUpVote_UserReact_ApiView,
  PostDownVote_UserReact_ApiView,
)


app_name = 'impressions'
router = routers.SimpleRouter()

router.register(r'emoji', Emoji_ApiView)

urlpatterns = [
  path('i/<int:post_id>/emoji/<int:emoji_id>/', PostEmoji_UserReact_ApiView.as_view(), name='user-react-emoji-to-post'),
  path('i/<int:post_id>/up/', PostUpVote_UserReact_ApiView.as_view(), name='user-react-upvote-to-post'),
  path('i/<int:post_id>/down/', PostDownVote_UserReact_ApiView.as_view(), name='user-react-downvote-to-post'),
  
  path('emojis/', Emoji_UserList_ApiView.as_view(), name='user-list-emoji'),
  
] + router.urls

