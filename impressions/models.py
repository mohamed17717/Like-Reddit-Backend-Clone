from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.contrib.auth import get_user_model
from notifications.models import NotificationSender

from posts.models import Post


User = get_user_model()

# W: Admin or Static | R: Anyone 
class Emoji(models.Model):
  name = models.CharField(max_length=16)

  class Meta:
    verbose_name = 'Emoji'
    verbose_name_plural = 'Emojis'

  def __str__(self):
    return self.name

# W: Anyone | R: Anyone
class PostEmoji(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='emojis')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emojis')
  emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE, related_name='post_emojis')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )

  class Meta:
    verbose_name = 'PostEmoji'
    verbose_name_plural = 'PostEmojis'

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_emoji_impression')
    ]

  def __str__(self):
    return f'{self.user} -> ({self.emoji}) -> {self.post}'

  def get_notification_url(self):
    return self.post.get_absolute_url()
  def get_notification_message(self):
    return f'{self.user.username} has reacted to your post by {self.emoji.name}.'

# W: Anyone | R: Anyone
class PostUpVote(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='upvotes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )

  class Meta:
    verbose_name = 'PostUpVote'
    verbose_name_plural = 'PostUpVotes'

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_upvote_impression')
    ]

  def __str__(self):
    return f'{self.user} -> {self.post}'

  def get_notification_url(self):
    return self.post.get_absolute_url()
  def get_notification_message(self):
    return f'{self.user.username} has upvoted your post.'

# W: Anyone | R: Anyone
class PostDownVote(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='downvotes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvotes')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )

  class Meta:
    verbose_name = 'PostDownVote'
    verbose_name_plural = 'PostDownVotes'

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_downvote_impression')
    ]

  def __str__(self):
    return f'{self.user} -> {self.post}'

  def get_notification_url(self):
    return self.post.get_absolute_url()
  def get_notification_message(self):
    return f'{self.user.username} has downvoted your post.'