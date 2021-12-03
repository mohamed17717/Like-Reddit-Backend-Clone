from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation

from posts.models import Post
from categories.models import SubCategory
from privates.models import PrivateContent


User = get_user_model()


# W: Static | R: Admin
class ThreadState(models.Model):
  state = models.CharField(max_length=32)

  class Meta:
    verbose_name = 'ThreadState'
    verbose_name_plural = 'ThreadStates'

  def __str__(self):
    return self.state


  @classmethod
  def get_value_obj(cls, value) -> int:
    obj = cls.objects.get_or_create(state=value)[0].pk
    return obj

  @classmethod
  def get_default_obj(cls):
    default_setting = ThreadDefaultSetting.objects.all().first()
    if default_setting:
      obj = default_setting.default_thread_state.pk
    else:
      obj = cls.get_value_obj('active')
    return obj


# W: Anyone | R: Anyone
class Thread(models.Model):
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread')
  title = models.CharField(max_length=128)
  category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='threads')
  state = models.ForeignKey(ThreadState, on_delete=models.SET_DEFAULT, default=ThreadState.get_default_obj, related_name='threads')

  description = models.TextField(blank=True, null=True)

  visits_count = models.PositiveIntegerField(default=0)
  comments_count = models.PositiveIntegerField(default=0)

  # generic field private
  private = GenericRelation(PrivateContent, object_id_field="content_id", related_query_name="thread")

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Thread'
    verbose_name_plural = 'Threads'
    ordering = ['-id']

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("threads:thread-retrieve", kwargs={"thread_id": self.pk})

  @property
  def is_private(self):
    return bool(self.private.first()) or self.category.is_private

# W: Anyone | R: Anyone
class ThreadPost(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread_post')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadPost'
    verbose_name_plural = 'ThreadPosts'

    ordering = ['-created']


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
  default_thread_state =  models.OneToOneField(ThreadState, on_delete=models.CASCADE, related_name='default_state')
  is_posting_active = models.BooleanField(default=True)

  class Meta:
    verbose_name = 'ThreadDefaultSetting'
    verbose_name_plural = 'ThreadDefaultSettings'

  def __str__(self):
    return 'Set Thread Settings'


# W: Runtime | R: Runtime
class ThreadUserVisit(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='visits')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visits')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadUserVisit'
    verbose_name_plural = 'ThreadUserVisits'

  def __str__(self):
    return f'{self.user} -> {self.thread}'


# W: Admin | R: Anyone
class Flair(models.Model):
  title = models.CharField(max_length=128)

  class Meta:
    verbose_name = 'Flair'
    verbose_name_plural = 'Flairs'

  def __str__(self):
    return self.title


# W: Anyone | R: Anyone
class ThreadFlair(models.Model):
  thread = models.OneToOneField(Thread, on_delete=models.CASCADE, related_name='flair')
  flair = models.ForeignKey(Flair, on_delete=models.CASCADE, related_name='threads')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'ThreadFlair'
    verbose_name_plural = 'ThreadFlairs'

  def __str__(self):
    return f'({self.flair}) {self.thread}'

