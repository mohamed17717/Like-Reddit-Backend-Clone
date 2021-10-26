from django.contrib import admin

from accounts.models import (
  UserProfile,
  UserVerified,
  UserPremium,
  UserBan,
)

admin.site.register(UserProfile)
admin.site.register(UserVerified)
admin.site.register(UserPremium)
admin.site.register(UserBan)

