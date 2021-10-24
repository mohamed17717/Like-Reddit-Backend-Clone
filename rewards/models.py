from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserKarma(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='karma')
  points = models.PositiveIntegerField(default=0)

  class Meta:
    verbose_name = 'UserKarma'
    verbose_name_plural = 'UsersKarma'

  def __str__(self):
    return f'{self.user} ({self.points})'

