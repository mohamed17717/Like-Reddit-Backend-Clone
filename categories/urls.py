from django.urls import path

from rest_framework import routers

from categories.views.admin_views import Category_ApiView, SubCategory_ApiView
from categories.views.anon_views import (
  Category_UserList_ApiView,
  SubCategory_ListOnCategory_ApiView
)

app_name = 'categories'

router = routers.SimpleRouter()

router.register(r'admin/category', Category_ApiView, 'admin-category')
router.register(r'admin/sub-category', SubCategory_ApiView, 'admin-sub-category')

urlpatterns = [
  path('category/', Category_UserList_ApiView.as_view(), name='user-list-categories'),
  path('category/<int:category_id>/', SubCategory_ListOnCategory_ApiView.as_view(), name='user-list-sub-categories'),

] + router.urls
