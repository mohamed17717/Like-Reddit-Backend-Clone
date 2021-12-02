from django.urls import path

from privates.views.admin_views import (
  PrivateContent_ToggleThreadPrivate_ApiView,
  PrivateContent_ToggleCategoryPrivate_ApiView,
  PrivateContent_ToggleSubCategoryPrivate_ApiView,
)

app_name = 'privates'

urlpatterns = [
  path('admin-thread/private/<int:thread_id>/', PrivateContent_ToggleThreadPrivate_ApiView.as_view(), name="make-thread-private"),
  path('admin-category/private/<int:category_id>/', PrivateContent_ToggleCategoryPrivate_ApiView.as_view(), name="make-category-private"),
  path('admin-category/sub/private/<int:sub_category_id>/', PrivateContent_ToggleSubCategoryPrivate_ApiView.as_view(), name="make-sub-category-private"),
]
