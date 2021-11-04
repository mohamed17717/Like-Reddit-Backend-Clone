from rest_framework import routers
from accounts.views import (
  UserVerified_ApiView,
  UserPremium_ApiView,
  UserBan_ApiView,
)

app_name = 'accounts'

router = routers.SimpleRouter()

router.register(r'u/verify', UserVerified_ApiView)
router.register(r'u/premium', UserPremium_ApiView)
router.register(r'u/ban', UserBan_ApiView)

urlpatterns = router.urls
