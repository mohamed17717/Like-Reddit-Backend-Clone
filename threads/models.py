from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post
from categories.models import SubCategory


User = get_user_model()

# TODO:
#   set counters for threads etc...
#   signal for user visit


# W: Static | R: Admin
class ThreadStates(models.Model):
  state = models.CharField(max_length=32)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.state


  @classmethod
  def get_value_obj(cls, value) -> int:
    obj = cls.objects.get_or_create(state=value)[0].pk
    return obj

  @classmethod
  def get_active_obj(cls): return cls.get_value_obj('active')

  @classmethod
  def get_hide_obj(cls): return cls.get_value_obj('hide')

  @classmethod
  def get_soft_delete_obj(cls): return cls.get_value_obj('soft delete')

  @classmethod
  def get_pending_obj(cls): return cls.get_value_obj('pending')

  @classmethod
  def get_default_obj(cls):
    default = ThreadDefaultSetting.objects.all().first()
    default = default and default.pk or cls.get_active_obj()
    return default

# W: Anyone | R: Anyone
class Thread(models.Model):
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread')
  title = models.CharField(max_length=128)
  category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='threads')
  state = models.ForeignKey(ThreadStates, on_delete=models.SET_DEFAULT, default=ThreadStates.get_default_obj, related_name='threads')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'Thread'
    verbose_name_plural = 'Threads'

  def __str__(self):
    return self.title


# W: Anyone | R: Anyone
class ThreadPost(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread_post')

  class Meta:
    verbose_name = 'ThreadPost'
    verbose_name_plural = 'ThreadPosts'

  def __str__(self):
    return f'{self.post}'


# W: Admin | R: Anyone
class ThreadPin(models.Model):
  thread = models.OneToOneField(Thread, on_delete=models.CASCADE, related_name='pinned')

  class Meta:
    verbose_name = 'ThreadPin'
    verbose_name_plural = 'ThreadsPins'

  def __str__(self):
    return f'{self.thread}'


# W: Static | R: Admin
class ThreadDefaultSetting(models.Model):
  default_thread_state =  models.OneToOneField(ThreadStates, on_delete=models.SET_DEFAULT, default=ThreadStates.get_active_obj, related_name='default_state')
  is_posting_active = models.BooleanField(default=True)

  class Meta:
    verbose_name = 'ThreadDefaultSetting'
    verbose_name_plural = 'ThreadDefaultSettings'

  def __str__(self):
    return 'Set Thread Settings'




class ThreadUserVisit(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='visits')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visits')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadUserVisit'
    verbose_name_plural = 'ThreadUserVisits'

  def __str__(self):
    return f'{self.user} -> {self.thread}'

class Flair(models.Model):
  title = models.CharField(max_length=128)

  class Meta:
    verbose_name = 'Flair'
    verbose_name_plural = 'Flairs'

  def __str__(self):
    return self.title


class ThreadFlair(models.Model):
  thread = models.OneToOneField(Thread, on_delete=models.CASCADE, related_name='flair')
  flair = models.ForeignKey(Flair, on_delete=models.CASCADE, related_name='threads')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadFlair'
    verbose_name_plural = 'ThreadFlairs'

  def __str__(self):
    return f'({self.flair}) {self.thread}'





