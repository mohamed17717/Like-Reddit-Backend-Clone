from django.contrib import admin

from .models import NotificationType
from .models import NotificationMessage
from .models import Notification
from .models import NotificationSender

admin.site.register(NotificationType)
admin.site.register(NotificationMessage)
admin.site.register(Notification)
admin.site.register(NotificationSender)

