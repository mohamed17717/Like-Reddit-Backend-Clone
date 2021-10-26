from django.contrib import admin

from follows.models import UserFollow, ThreadFollow

admin.site.register(UserFollow)
admin.site.register(ThreadFollow)

