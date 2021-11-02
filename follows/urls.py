from django.urls import path

from follows.views import (
  UserFollow_ToggleFollow_ApiView,
  UserFollow_CheckFollow_ApiView,
  UserFollow_ListFollows_ApiView,
  UserFollow_ListFollowers_ApiView,

  ThreadFollow_ToggleFollow_ApiView,
)

app_name = 'follows'

urlpatterns = [
  path('u/<str:username>/follow/', UserFollow_ToggleFollow_ApiView.as_view(), name="user-follow-toggle"),
  path('u/<str:username>/check-follow/', UserFollow_CheckFollow_ApiView.as_view(), name="user-follow-check"),
  path('following/', UserFollow_ListFollows_ApiView.as_view(), name="user-following-list"),
  path('followers/', UserFollow_ListFollowers_ApiView.as_view(), name="user-followers-list"),

  path('t/<int:thread_id>/follow/', ThreadFollow_ToggleFollow_ApiView.as_view(), name="thread-follow-toggle"),
]
