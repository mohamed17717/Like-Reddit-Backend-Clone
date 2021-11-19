from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.expressions import F
from django.db.models.query_utils import Q

from threads.models import Thread


User = get_user_model()


# W: Anyone | R: Anyone
class UserFollow(models.Model):
  target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers')
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_targets')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'UserFollow'
    verbose_name_plural = 'UserFollows'

    constraints = [
      models.UniqueConstraint(fields=['target', 'follower'], name='user_follow_user_once'),
      models.CheckConstraint(check=~Q(target=F('follower')), name='user_cant_follow_himself')
    ]

  def __str__(self):
    return f'New Follower ({self.follower}) for you ({self.target})'


# W: Anyone | R: Anyone
class ThreadFollow(models.Model):
  target = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread_followers')
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_targets')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadFollow'
    verbose_name_plural = 'ThreadFollows'

    constraints = [
      models.UniqueConstraint(fields=['target', 'follower'], name='user_follow_thread_once')
    ]

  def __str__(self):
    return f'{self.follower} -> {self.target}'

