from django.urls import path

from rest_framework import routers

from categories.views.admin_views import Category_ApiView, SubCategory_ApiView
from categories.views.anon_views import (
  Category_UserList_ApiView,
  SubCategory_ListOnCategory_ApiView
)

app_name = 'categories'

router = routers.SimpleRouter()

router.register(r'admin-category', Category_ApiView)
router.register(r'admin-category/sub', SubCategory_ApiView)

urlpatterns = [
  path('category/', Category_UserList_ApiView.as_view(), name='user-list-categories'),
  path('category/<int:category_id>/', SubCategory_ListOnCategory_ApiView.as_view(), name='user-list-sub-categories-on-category'),

] + router.urls
