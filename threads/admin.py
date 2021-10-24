from django.contrib import admin

from .models import ThreadStates
from .models import Thread
from .models import ThreadPost
from .models import ThreadPin
from .models import ThreadDefaultSetting


admin.site.register(ThreadStates)
admin.site.register(Thread)
admin.site.register(ThreadPost)
admin.site.register(ThreadPin)
admin.site.register(ThreadDefaultSetting)

