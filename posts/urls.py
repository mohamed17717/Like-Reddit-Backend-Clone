from django.urls import path

from rest_framework import routers
from posts.views import (
  Post_OwnerActions_ApiView,
  Post_CreateReplay_ApiView,
  PostReplay_ListPostReplays_ApiView,

  Post_AdminUpdateState_ApiView
)

app_name = 'posts'
router = routers.SimpleRouter()

router.register(r'p/actions', Post_OwnerActions_ApiView, 'post-owner-actions')


urlpatterns = [
  path('p/<int:post_id>/replay/', Post_CreateReplay_ApiView.as_view(), name='create-post-replay'),
  path('p/<int:post_id>/replays/', PostReplay_ListPostReplays_ApiView.as_view(), name='list-post-replays'),

  path('p/<int:pk>/update-state/', Post_AdminUpdateState_ApiView.as_view(), name='post-update-state'),
  # path('p')

] + router.urls
