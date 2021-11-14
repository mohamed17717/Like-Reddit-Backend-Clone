from django.urls import path

from rewards.views.admin_views import (
  UserKarma_List_ApiView
)

app_name = 'rewards'

urlpatterns = [
  path('admin-user/list-on-karma/', UserKarma_List_ApiView.as_view(), name="list-users-on-karma"),
]
