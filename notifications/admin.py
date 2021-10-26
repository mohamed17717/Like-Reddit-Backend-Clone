from django.contrib import admin

from notifications.models import (
  NotificationType,
  NotificationMessage,
  Notification,
  NotificationSender,
)

admin.site.register(NotificationType)
admin.site.register(NotificationMessage)
admin.site.register(Notification)
admin.site.register(NotificationSender)

