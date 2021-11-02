from django.urls import path

from saves.views import (
  SavePost_ToggleSave_ApiView,
  SavePost_ListSaves_ApiView,
)

app_name = 'saves'

urlpatterns = [
  path('p/<int:post_id>/save/', SavePost_ToggleSave_ApiView.as_view(), name="save-post-toggle"),
  path('p/saves/', SavePost_ListSaves_ApiView.as_view(), name="list-saved-posts"),
]
