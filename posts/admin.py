from django.contrib import admin

from posts.models import (
  PostConetntType,
  PostContent,
  Post,
  PostReplay,
)

admin.site.register(PostConetntType)
admin.site.register(PostContent)
admin.site.register(Post)
admin.site.register(PostReplay)

