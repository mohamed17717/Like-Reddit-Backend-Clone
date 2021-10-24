from django.contrib import admin

from .models import UserProfile
from .models import UserVerified
from .models import UserPremium
from .models import UserBan

admin.site.register(UserProfile)
admin.site.register(UserVerified)
admin.site.register(UserPremium)
admin.site.register(UserBan)

