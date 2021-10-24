from django.contrib import admin

from .models import PostConetntType
from .models import PostContent
from .models import PostState
from .models import Post
from .models import PostReplay

admin.site.register(PostConetntType)
admin.site.register(PostContent)
admin.site.register(PostState)
admin.site.register(Post)
admin.site.register(PostReplay)

