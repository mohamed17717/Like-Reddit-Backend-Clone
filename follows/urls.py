from django.urls import path

from follows.views.user_views import (
  UserFollow_ToggleFollow_ApiView,
  UserFollow_CheckFollow_ApiView,

  ThreadFollow_ToggleFollow_ApiView,
)

from follows.views.anon_views import (
  UserFollowersList_ApiView,
  UserFollowingList_ApiView,
)

app_name = 'follows'

urlpatterns = [
  path('follow/<str:username>/', UserFollow_ToggleFollow_ApiView.as_view(), name="user-follow-toggle"),
  path('follow/<str:username>/check/', UserFollow_CheckFollow_ApiView.as_view(), name="user-follow-check"),

  path('following/', UserFollowingList_ApiView.as_view(), name="current-user-following-list"),
  path('followers/', UserFollowersList_ApiView.as_view(), name="current-user-followers-list"),

  path('<str:username>/following/', UserFollowingList_ApiView.as_view(), name="user-following-list"),
  path('<str:username>/followers/', UserFollowersList_ApiView.as_view(), name="user-followers-list"),

  path('follow/thread/<int:thread_id>/', ThreadFollow_ToggleFollow_ApiView.as_view(), name="thread-follow-toggle"),
]
