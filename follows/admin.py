from django.contrib import admin

from .models import UserFollow
from .models import ThreadFollow

admin.site.register(UserFollow)
admin.site.register(ThreadFollow)

