from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from notifications.models import NotificationSender

User = get_user_model()

class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  profile_picture = models.ImageField(upload_to='static/user-profile-pic/', default='static/user-profile-pic/default.jpg')

  follower_count = models.PositiveIntegerField(default=0)
  following_count = models.PositiveIntegerField(default=0)

  class Meta:
    verbose_name = 'UserProfile'
    verbose_name_plural = 'UsersProfiles'

  def __str__(self):
    return self.user.username

  def get_absolute_url(self):
    return reverse("accounts:user-profile", kwargs={"username": self.user.username})

class UserVerified(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verified')

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )
  class Meta:
    verbose_name = 'UserVerified'
    verbose_name_plural = 'UsersVerified'
    ordering = ['id']

  def __str__(self):
    return self.user.username

  def get_notification_url(self):
    return None
  def get_notification_message(self):
    return f'Congrats, You are now a verified user.'

class UserPremium(models.Model):
  """ Has Access To Private Content """
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='premium')

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )
  class Meta:
    verbose_name = 'UserPremium'
    verbose_name_plural = 'UsersPremium'
    ordering = ['id']

  def __str__(self):
    return self.user.username

  def get_notification_url(self):
    return None
  def get_notification_message(self):
    return f'Congrats, You are now a premium user.'

class UserBan(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bans')
  days = models.PositiveIntegerField(default=1)
  start = models.DateField(auto_now_add=True)

  state = models.CharField(max_length=16, default='active')

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )

  class Meta:
    verbose_name = 'UserBan'
    verbose_name_plural = 'UsersBans'
    ordering = ['id']

  def __str__(self):
    return self.user.username

  def get_notification_url(self):
    return None
  def get_notification_message(self):
    return f'You are got banned for {self.days} days.'
