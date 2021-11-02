from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# W: Runtime | R: Anyone
class UserProfile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
  profile_picture = models.ImageField(upload_to='static/user-profile-pic/', default='static/user-profile-pic/default.jpg')

  class Meta:
    verbose_name = 'UserProfile'
    verbose_name_plural = 'UsersProfiles'

  def __str__(self):
    return self.user.username


# W: Admin | R: Anyone
class UserVerified(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='verified')

  class Meta:
    verbose_name = 'UserVerified'
    verbose_name_plural = 'UsersVerified'

  def __str__(self):
    return self.user.username



# W: Admin | R: Anyone
class UserPremium(models.Model):
  """ Has Access To Private Content """
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='premium')

  class Meta:
    verbose_name = 'UserPremium'
    verbose_name_plural = 'UsersPremium'

  def __str__(self):
    return self.user.username


# W: Admin | R: Anyone
class UserBan(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bans')
  days = models.PositiveIntegerField(default=1)
  start = models.DateField(auto_now_add=True)

  class Meta:
    verbose_name = 'UserBan'
    verbose_name_plural = 'UsersBans'

  def __str__(self):
    return self.user.username


