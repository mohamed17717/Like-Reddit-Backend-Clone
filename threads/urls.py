from django.urls import path
from rest_framework import routers

from threads.views import (
  Thread_Owner_ApiView,

  Thread_Retrieve_ApiView,

  ThreadPin_Toggle_ApiView,
  ThreadPin_List_ApiView,

  Thread_ListOnSubCategory_ApiView,

  Thread_AdminUpdateState_ApiView,

  Thread_Commenting_ApiView,

  Thread_OwnerUpdateStatePrivate_ApiView,
  Thread_OwnerUpdateStatePublic_ApiView
)

app_name = 'threads'
router = routers.SimpleRouter()

router.register(r'th/owner', Thread_Owner_ApiView, 'thread-owner')

urlpatterns = [
  path('th/<int:pk>/', Thread_Retrieve_ApiView.as_view(), name="thread-retrieve"),
  path('th/list/<int:sub_category_id>/', Thread_ListOnSubCategory_ApiView.as_view(), name="list-threads-category"),
  path('th/<int:pk>/comment/', Thread_Commenting_ApiView.as_view(), name="thread-commenting"),

  path('th/<int:thread_id>/pin/', ThreadPin_Toggle_ApiView.as_view(), name='pin-thread'),
  path('th/pinned/', ThreadPin_List_ApiView.as_view(), name='list-pinned-threads'),
  path('th/<int:pk>/update-state/', Thread_AdminUpdateState_ApiView.as_view(), name='admin-update-thread-state'),

  path('th/<int:thread_id>/private/', Thread_OwnerUpdateStatePrivate_ApiView.as_view(), name='owner-make-post-private'),
  path('th/<int:thread_id>/public/', Thread_OwnerUpdateStatePublic_ApiView.as_view(), name='owner-make-post-public'),
] + router.urls

