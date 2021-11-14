from django.urls import path

from rest_framework import routers
from categories.views.admin_views import Category_ApiView, SubCategory_ApiView
from categories.views.user_views import (
  Category_UserList_ApiView,
  SubCategory_UserList_ApiView,
)

app_name = 'categories'

router = routers.SimpleRouter()

router.register(r'admin-category', Category_ApiView)
router.register(r'admin-category/sub', SubCategory_ApiView)

urlpatterns = [
  path('categories/', Category_UserList_ApiView.as_view(), 'user-list-categories'),
  path('categories/sub/', SubCategory_UserList_ApiView.as_view(), 'user-list-sub-categories'),

] + router.urls
