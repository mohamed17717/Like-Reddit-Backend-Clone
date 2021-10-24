from django.contrib import admin

from .models import ThreadStates
from .models import Thread
from .models import ThreadPost

admin.site.register(ThreadStates)
admin.site.register(Thread)
admin.site.register(ThreadPost)

