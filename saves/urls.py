from django.urls import path

from saves.views.owner_views import (
  SavePost_ToggleSave_ApiView,
  SavePost_ListSaves_ApiView,
)

app_name = 'saves'

urlpatterns = [
  path('post/save/<int:post_id>/', SavePost_ToggleSave_ApiView.as_view(), name="save-post-toggle"),
  path('post/saves/', SavePost_ListSaves_ApiView.as_view(), name="list-saved-posts"),
]
