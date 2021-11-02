from django.urls import path

from rewards.views import (
  UserKarma_List_ApiView
)

app_name = 'rewards'

urlpatterns = [
  path('u/list/karma/', UserKarma_List_ApiView.as_view(), name="list-users-on-karma"),
]
