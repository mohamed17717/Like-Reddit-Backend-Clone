from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# TODO: 
#   signal update user total when update user action
#   signal create user total points when user register 
#   signal to add calc user reward every time points increase
#   signal to send notification whenever user get reward


# W: Admin | R: Anyone
class Reward(models.Model):
  title = models.CharField(max_length=128)
  icon = models.ImageField(upload_to='rewards_icons/')
  description = models.TextField(blank=True, null=True)
  points = models.IntegerField()

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'Reward'
    verbose_name_plural = 'Rewards'

  def __str__(self):
    return self.title


# W: (title: Static, points: Admin)  | R: Admin
class RewardTodoAction(models.Model):
  # Actions that make user get rewards
  title = models.CharField(max_length=128)
  points = models.IntegerField()

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'RewardTodoAction'
    verbose_name_plural = 'RewardTodoAction'

  def __str__(self):
    return self.title


# W: Anyone | R: No
class UserAction(models.Model):
  # actions user has done to obtain points -- count is how many action done
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actions')
  action = models.ForeignKey(RewardTodoAction, on_delete=models.CASCADE, related_name='actions')
  count = models.IntegerField(default=0)

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'UserAction'
    verbose_name_plural = 'UserActions'

  def __str__(self):
    return f'{self.user.username} ({self.action.title})'


# W: Runtime | R: Anyone
class UserReward(models.Model):
  # rewards user has obtain
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rewards')
  reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='rewards')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'UserReward'
    verbose_name_plural = 'UserRewards'

  def __str__(self):
    return f'{self.user.username} ({self.reward.title})'


# W: Runtime | R: Anyone
class UserTotalPoints(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_points')
  points = models.IntegerField(default=0)

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'UserTotalPoints'
    verbose_name_plural = 'UsersTotalPoints'

  def __str__(self):
    return f'{self.user.username} ({self.points})'


# W: Static | R: Admin
class RewardPossibleFeature(models.Model):
  title = models.CharField(max_length=128)

  class Meta:
    verbose_name = 'RewardPossibleFeature'
    verbose_name_plural = 'RewardPossibleFeature'

  def __str__(self):
    return self.title


# W: Admin | R: Anyone
class RewardFeature(models.Model):
  reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='reward_features')
  feature = models.ForeignKey(RewardPossibleFeature, on_delete=models.CASCADE, related_name='reward_features')

  class Meta:
    verbose_name = 'RewardFeature'
    verbose_name_plural = 'RewardFeatures'

  def __str__(self):
    return f'{self.reward} ({self.feature})'

