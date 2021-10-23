from django.db import models
from django.contrib.auth import get_user_model

from threads.models import Thread


User = get_user_model()


# W: Anyone | R: Anyone
class UserFollow(models.Model):
  target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_followers')
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_targets')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'UserFollow'
    verbose_name_plural = 'UserFollows'

  def __str__(self):
    return f'{self.follower} -> {self.target}'


# W: Anyone | R: Anyone
class ThreadFollow(models.Model):
  target = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='thread_followers')
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='thread_targets')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadFollow'
    verbose_name_plural = 'ThreadFollows'

  def __str__(self):
    return f'{self.follower} -> {self.target}'

