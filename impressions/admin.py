from django.contrib import admin

from impressions.models import (
  Emoji,
  PostEmoji,
  PostUpVote,
  PostDownVote,
)

admin.site.register(Emoji)
admin.site.register(PostEmoji)
admin.site.register(PostUpVote)
admin.site.register(PostDownVote)

