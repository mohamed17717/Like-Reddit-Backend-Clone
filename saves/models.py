from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()

# W: Anyone | R: Anyone
class SavePost(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_posts')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='saved_posts')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'SavePost'
    verbose_name_plural = 'SavePosts'
    ordering = ['-created']

    constraints = [
      models.UniqueConstraint(fields=['post', 'user'], name='user_post_unique_save_post')
    ]

  def __str__(self):
    return f'{self.user} -> {self.post}'
