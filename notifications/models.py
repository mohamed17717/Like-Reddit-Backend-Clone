from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# TODO
#   collapse notifications like upvote etc...
#   notification seen field


User = get_user_model()

# W: Static | R: Runtime
class NotificationType(models.Model):
  type = models.CharField(max_length=64)

  class Meta:
    verbose_name = 'NotificationType'
    verbose_name_plural = 'NotificationTypes'

  def __str__(self):
    return self.type


# W: Runtime | R: Runtime
class NotificationSender(models.Model):
  limits = models.Q(app_label='follows', model='UserFollow') | \
    models.Q(app_label='posts', model='PostReplay') | \
    models.Q(app_label='threads', model='Thread') | \
    models.Q(app_label='threads', model='ThreadPost') | \
    models.Q(app_label='impressions', model='PostUpVote') | \
    models.Q(app_label='impressions', model='PostDownVote') | \
    models.Q(app_label='impressions', model='PostEmoji') | \
    models.Q(app_label='accounts', model='UserBan') | \
    models.Q(app_label='accounts', model='UserPremium') | \
    models.Q(app_label='accounts', model='UserVerified')

  sender_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limits)
  sender_id = models.PositiveIntegerField()
  sender_object = GenericForeignKey('sender_type', 'sender_id')

  class Meta:
    verbose_name = 'NotificationSender'
    verbose_name_plural = 'NotificationSenders'

  def __str__(self):
    return f'({self.notification.pk}) {self.sender_object}'


# W: Anyone (signals) | R: Anyone
class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
  type = models.ForeignKey(NotificationType, on_delete=models.CASCADE, related_name='notifications')

  is_viewed = models.BooleanField(default=False)

  # generic field private
  sender = GenericRelation(NotificationSender, object_id_field="sender_id", related_query_name="notification")

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  @property
  def message(self):
    sender = self.senders.all().first()

    message = ''
    if sender.sender_object:
      message = sender.sender_object.get_message()
    else:
      self.delete()
    return message

  class Meta:
    verbose_name = 'Notification'
    verbose_name_plural = 'Notifications'

    ordering = ['-created']

  def __str__(self):
    return f'{self.user} ({self.type})'


