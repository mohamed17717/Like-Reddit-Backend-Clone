from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


User = get_user_model()

# W: Static | R: Runtime
class NotificationType(models.Model):
  type = models.CharField(max_length=64)

  class Meta:
    verbose_name = 'NotificationType'
    verbose_name_plural = 'NotificationTypes'

  def __str__(self):
    return self.type


# W: Static | R: Runtime
class NotificationMessage(models.Model):
  type = models.ForeignKey(NotificationType, on_delete=models.CASCADE, related_name='messages')
  message_format = models.TextField()

  class Meta:
    verbose_name = 'NotificationMessage'
    verbose_name_plural = 'NotificationMessages'

  def __str__(self):
    return f'{self.message_format} ({self.type})'


# W: Anyone (signals) | R: Anyone
class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
  type = models.ForeignKey(NotificationType, on_delete=models.CASCADE, related_name='notifications')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'Notification'
    verbose_name_plural = 'Notifications'

  def __str__(self):
    return f'{self.user} ({self.type})'


# W: Runtime | R: Runtime
class NotificationSender(models.Model):
  notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='senders')

  # limits = models.Q(app_label='threads', model='Thread') | \
  #   models.Q(app_label='categories', model='Category') | \
  #   models.Q(app_label='categories', model='SubCategory')
  # limit_choices_to=limits

  sender_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  sender_id = models.PositiveIntegerField()
  sender_object = GenericForeignKey('sender_type', 'sender_id')

  class Meta:
    verbose_name = 'NotificationSender'
    verbose_name_plural = 'NotificationSenders'

  def __str__(self):
    return f'({self.notification.pk}) {self.sender_object}'

