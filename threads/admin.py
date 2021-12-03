from django.contrib import admin

from threads.models import (
  Thread,
  ThreadPost,
  ThreadPin,
  ThreadDefaultSetting,
  ThreadUserVisit,
  Flair,
  ThreadFlair,
)

admin.site.register(Thread)
admin.site.register(ThreadPost)
admin.site.register(ThreadPin)
admin.site.register(ThreadDefaultSetting)
admin.site.register(ThreadUserVisit)
admin.site.register(Flair)
admin.site.register(ThreadFlair)

