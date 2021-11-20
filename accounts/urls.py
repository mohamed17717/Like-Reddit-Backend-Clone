from django.urls import path, include
from rest_framework import routers

from accounts.views.admin_views import (
  UserVerified_ApiView,
  UserPremium_ApiView,
  UserBan_ApiView,
)

from accounts.views.anon_views import UserProfile_ApiView

app_name = 'accounts'

router = routers.SimpleRouter()

router.register(r'admin-user/verify', UserVerified_ApiView)
router.register(r'admin-user/premium', UserPremium_ApiView)
router.register(r'admin-user/ban', UserBan_ApiView)

urlpatterns = [
  path('rest-auth/', include('rest_framework.urls')),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.jwt')),

  path('user/<str:username>/', UserProfile_ApiView.as_view(), name='user-profile')
] + router.urls
