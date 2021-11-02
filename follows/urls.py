from django.urls import path

from follows.views import (
  UserFollow_ToggleFollow_ApiView,
  UserFollow_CheckFollow_ApiView,
  UserFollow_ListFollows_ApiView,
  UserFollow_ListFollowers_ApiView,
)

app_name = 'follows'

urlpatterns = [
  path('u/<str:username>/follow/', UserFollow_ToggleFollow_ApiView.as_view(), name="follow-toggle"),
  path('u/<str:username>/check-follow/', UserFollow_CheckFollow_ApiView.as_view(), name="follow-check"),
  path('following/', UserFollow_ListFollows_ApiView.as_view(), name="following-list"),
  path('followers/', UserFollow_ListFollowers_ApiView.as_view(), name="followers-list"),

]
