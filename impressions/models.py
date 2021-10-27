from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

# TODO:
#   may be set upVote counter in post itself better than calculate every time
#   user cant upvote and downvote the same post 


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

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'PostEmoji'
    verbose_name_plural = 'PostEmojis'

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_emoji_impression')
    ]

  def __str__(self):
    return f'{self.user} -> ({self.emoji}) -> {self.post}'



# W: Anyone | R: Anyone
class PostUpVote(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='upvotes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='upvotes')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'PostUpVote'
    verbose_name_plural = 'PostUpVotes'

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_upvote_impression')
    ]

  def __str__(self):
    return f'{self.user} -> {self.post}'


# W: Anyone | R: Anyone
class PostDownVote(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='downvotes')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downvotes')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'PostDownVote'
    verbose_name_plural = 'PostDownVotes'

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_downvote_impression')
    ]

  def __str__(self):
    return f'{self.user} -> {self.post}'

