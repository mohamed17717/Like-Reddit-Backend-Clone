from django.contrib import admin

from .models import Emoji
from .models import PostEmoji
from .models import PostUpVote
from .models import PostDownVote


admin.site.register(Emoji)
admin.site.register(PostEmoji)
admin.site.register(PostUpVote)
admin.site.register(PostDownVote)

