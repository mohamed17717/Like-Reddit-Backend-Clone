from django.urls import path

from rest_framework import routers

from posts.views.admin_views import Post_AdminUpdateState_ApiView
from posts.views.owner_views import Post_OwnerActions_ApiView
from posts.views.user_views import Post_CreateReplay_ApiView
from posts.views.anon_views import PostReplay_ListPostReplays_ApiView


app_name = 'posts'
router = routers.SimpleRouter()

router.register(r'own/post/actions', Post_OwnerActions_ApiView, 'post-owner-actions')


urlpatterns = [
  path('post/<int:post_id>/replay/', Post_CreateReplay_ApiView.as_view(), name='create-post-replay'),
  path('post/<int:post_id>/replays/', PostReplay_ListPostReplays_ApiView.as_view(), name='list-post-replays'),

  path('admin-post/<int:post_id>/update-state/', Post_AdminUpdateState_ApiView.as_view(), name='post-update-state'),
] + router.urls
