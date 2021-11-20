from django.urls import path
from rest_framework import routers

from threads.views.owner_views import (
  Thread_Owner_ApiView,
  Thread_OwnerUpdateStatePrivate_ApiView,
  Thread_OwnerUpdateStatePublic_ApiView
)
from threads.views.user_views import Thread_Commenting_ApiView
from threads.views.anon_views import (
  Thread_Retrieve_ApiView,
  Thread_ListOnSubCategory_ApiView,
  Thread_LatestList_ApiView,
)
from threads.views.admin_views import (
  ThreadPin_Toggle_ApiView,
  ThreadPin_List_ApiView,
  Thread_AdminUpdateState_ApiView,
)


app_name = 'threads'
router = routers.SimpleRouter()

router.register(r'own/thread', Thread_Owner_ApiView, 'thread-owner')

urlpatterns = [
  path('thread/<int:thread_id>/comment/', Thread_Commenting_ApiView.as_view(), name="thread-commenting"),

  path('thread/<int:thread_id>/', Thread_Retrieve_ApiView.as_view(), name="thread-retrieve"),
  path('thread/list/<int:sub_category_id>/', Thread_ListOnSubCategory_ApiView.as_view(), name="list-threads-category"),
  path('thread/latest/', Thread_LatestList_ApiView.as_view(), name='latest-threads'),

  path('admin-thread/<int:thread_id>/pin/', ThreadPin_Toggle_ApiView.as_view(), name='pin-thread'),
  path('admin-thread/pinned/', ThreadPin_List_ApiView.as_view(), name='list-pinned-threads'),
  path('admin-thread/<int:thread_id>/update-state/', Thread_AdminUpdateState_ApiView.as_view(), name='admin-update-thread-state'),

  path('own/thread/<int:thread_id>/private/', Thread_OwnerUpdateStatePrivate_ApiView.as_view(), name='owner-make-post-private'),
  path('own/thread/<int:thread_id>/public/', Thread_OwnerUpdateStatePublic_ApiView.as_view(), name='owner-make-post-public'),

] + router.urls

