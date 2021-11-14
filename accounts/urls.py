from django.urls import path, include
from rest_framework import routers

from accounts.views.admin_views import (
  UserVerified_ApiView,
  UserPremium_ApiView,
  UserBan_ApiView,
)

app_name = 'accounts'

router = routers.SimpleRouter()

router.register(r'u/verify', UserVerified_ApiView)
router.register(r'u/premium', UserPremium_ApiView)
router.register(r'u/ban', UserBan_ApiView)

urlpatterns = [
  path('api-auth/', include('rest_framework.urls')),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.jwt')),
] + router.urls
