from django.contrib import admin

from notifications.models import (
  NotificationType,
  Notification,
  NotificationSender,
)

admin.site.register(NotificationType)
admin.site.register(Notification)
admin.site.register(NotificationSender)

