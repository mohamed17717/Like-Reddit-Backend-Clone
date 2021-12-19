from django.db import models
from django.contrib.auth import get_user_model

from posts.managers import PostManager
from states.models import ExistingState

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


# W: Anyone | R: Anyone
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
  post_content = models.OneToOneField(PostContent, on_delete=models.PROTECT, related_name='post')

  existing_state = models.ForeignKey(ExistingState, on_delete=models.SET_DEFAULT, default=ExistingState.get_default_obj, related_name='posts')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  upvote_count = models.PositiveIntegerField(default=0)
  downvote_count = models.PositiveIntegerField(default=0)
  emoji_count = models.PositiveIntegerField(default=0)
  replays_count = models.PositiveIntegerField(default=0)

  objects = PostManager()

  class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'

  def __str__(self):
    return f'({self.user}) ({self.created}) {self.post_content.content[:60]}'

  def get_absolute_url(self):
    # thread_deep2 = self.replay.post if hasattr(self, 'replay') else self
    # thread_deep1 = thread_deep2.thread_post if hasattr(thread_deep2, 'thread_post') else self
    # thread = thread_deep1.thread
    thread = self.get_thread()
    return f'{thread.get_absolute_url()}#post{self.pk}'

  def get_thread_title(self):
    thread = self.get_thread()
    return thread.title

  def get_thread_relation(self):
    return self.get_relation()

  def get_thread(self):
    post = self

    its_post_for_replay = hasattr(post, 'replay')
    if its_post_for_replay:
      post = post.replay.post

    its_post_for_comment = hasattr(post, 'thread_post')
    if its_post_for_comment:
      post = post.thread_post

    thread = post.thread
    return thread

  def get_relation(self):
    possible_relations = ['replay', 'thread_post', 'thread']

    for rel in possible_relations:
      if hasattr(self, rel):
        return rel


# W: Anyone | R: Anyone
class PostReplay(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='replays')
  replay = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='replay')

  class Meta:
    verbose_name = 'PostReplay'
    verbose_name_plural = 'PostReplays'

  def __str__(self):
    return f'{self.replay}'

  def get_notification_url(self):
    return self.post.get_absolute_url()
  def get_notification_message(self):
    return f'{self.post.user.username} is replied to you, on ({self.post.get_thread_title()}).'


