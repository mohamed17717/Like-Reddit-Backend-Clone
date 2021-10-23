from django.db import models
from django.contrib.auth import get_user_model

from threads.models import Thread

User = get_user_model()


# W: Static | R: Runtime
class PostConetntType(models.Model):
  type = models.CharField(max_length=32)

  class Meta:
    verbose_name = 'PostConetntType'
    verbose_name_plural = 'PostConetntTypes'

  def __str__(self):
    return self.type

  @classmethod
  def get_value_obj(cls, value) -> int:
    obj = cls.objects.get_or_create(type=value)[0].pk
    return obj

  @classmethod
  def get_text_obj(cls): return cls.get_value_obj('text')


# W: Anyone | R: Anyone
class PostContent(models.Model):
  content = models.TextField()
  type = models.ForeignKey(PostConetntType, on_delete=models.SET_DEFAULT, default=PostConetntType.get_text_obj, related_name='contents')

  class Meta:
    verbose_name = 'PostContent'
    verbose_name_plural = 'PostContents'

  def __str__(self):
    return f'({self.type}) {self.content[:50]}...'

  def get_content(self):
    renders = {
      'markdown': lambda md: 'md_to_html(md)',
      'html': lambda html: html,
      'text': lambda text: ''.join([f'<p>{t}</p>' for t in text.split('\n')]),
    }
    return self.content


# W: Static | R: Admin
class PostState(models.Model):
  name = models.CharField(max_length=32)

  @classmethod
  def get_value_obj(cls, value) -> int:
    obj = cls.objects.get_or_create(name=value)[0].pk
    return obj

  @classmethod
  def get_active_obj(cls): return cls.get_value_obj('active')

  @classmethod
  def get_hide_obj(cls): return cls.get_value_obj('hide')

  @classmethod
  def get_soft_delete_obj(cls): return cls.get_value_obj('soft delete')

  class Meta:
    verbose_name = 'PostState'
    verbose_name_plural = 'PostStates'

  def __str__(self):
    return self.name


# W: Anyone | R: Anyone
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  post_content = models.OneToOneField(PostContent, on_delete=models.PROTECT, related_name='post')

  description = models.CharField(max_length=128, blank=True, null=True)
  state = models.ForeignKey(PostState, on_delete=models.SET_DEFAULT, default=PostState.get_active_obj, related_name='posts')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return f'({self.user}) {self.description}'


# W: Anyone | R: Anyone
class PostReplay(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replays')
  replay = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='replay')

  class Meta:
    verbose_name = 'PostReplay'
    verbose_name_plural = 'PostReplays'

  def __str__(self):
    return self.replay


# W: Anyone | R: Anyone
class ThreadPost(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread_post')

  class Meta:
    verbose_name = 'ThreadPost'
    verbose_name_plural = 'ThreadPosts'

  def __str__(self):
    return self.replay





