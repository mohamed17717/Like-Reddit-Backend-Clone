from django.urls import path

from privates.views.admin_views import (
  PrivateContent_ToggleThreadPrivate_ApiView,
  PrivateContent_ToggleCategoryPrivate_ApiView,
  PrivateContent_ToggleSubCategoryPrivate_ApiView,
)

app_name = 'privates'

urlpatterns = [
  path('admin/thread/<int:thread_id>/private/', PrivateContent_ToggleThreadPrivate_ApiView.as_view(), name="make-thread-private"),
  path('admin/category/<int:category_id>/private/', PrivateContent_ToggleCategoryPrivate_ApiView.as_view(), name="make-category-private"),
  path('admin/sub-category/<int:sub_category_id>/private/', PrivateContent_ToggleSubCategoryPrivate_ApiView.as_view(), name="make-sub-category-private"),
]
