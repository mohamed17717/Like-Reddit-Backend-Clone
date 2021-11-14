from django.urls import path

from follows.views.user_views import (
  UserFollow_ToggleFollow_ApiView,
  UserFollow_CheckFollow_ApiView,

  ThreadFollow_ToggleFollow_ApiView,
)

from follows.views.owner_views import (
  UserFollow_ListFollows_ApiView,
  UserFollow_ListFollowers_ApiView,
)

app_name = 'follows'

urlpatterns = [
  path('user/follow/<str:username>/', UserFollow_ToggleFollow_ApiView.as_view(), name="user-follow-toggle"),
  path('user/follow/<str:username>/check/', UserFollow_CheckFollow_ApiView.as_view(), name="user-follow-check"),

  path('user/following/', UserFollow_ListFollows_ApiView.as_view(), name="user-following-list"),
  path('user/followers/', UserFollow_ListFollowers_ApiView.as_view(), name="user-followers-list"),

  path('thread/follow/<int:thread_id>/', ThreadFollow_ToggleFollow_ApiView.as_view(), name="thread-follow-toggle"),
]
