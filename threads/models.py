from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from notifications.models import NotificationSender

from posts.models import Post
from categories.models import SubCategory
from privates.models import PrivateContent
from states.models import PendingState, PrivacyState
from threads.managers import ThreadManager, ThreadPinManager


User = get_user_model()


# W: Static | R: Admin
class ThreadDefaultSetting(models.Model):
  default_pending_state =  models.OneToOneField(PendingState, on_delete=models.CASCADE, related_name='default_state')
  is_posting_active = models.BooleanField(default=True)

  class Meta:
    verbose_name = 'ThreadDefaultSetting'
    verbose_name_plural = 'ThreadDefaultSettings'

  def __str__(self):
    return 'Set Thread Settings'

  @classmethod
  def get_default_pending_state(cls):
    default_setting = cls.objects.first()
    obj_id = 1
    if default_setting:
      obj_id = default_setting.default_pending_state.pk

    return obj_id


# W: Anyone | R: Anyone
class Thread(models.Model):
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread')
  title = models.CharField(max_length=128)
  category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='threads')

  pending_state = models.ForeignKey(PendingState, on_delete=models.SET_DEFAULT, default=ThreadDefaultSetting.get_default_pending_state, related_name='threads')
  privacy_state = models.ForeignKey(PrivacyState, on_delete=models.SET_DEFAULT, default=PrivacyState.get_default_obj, related_name='threads')

  description = models.TextField(blank=True, null=True)

  visits_count = models.PositiveIntegerField(default=0)
  comments_count = models.PositiveIntegerField(default=0)

  # generic field private
  private = GenericRelation(PrivateContent, object_id_field="content_id", related_query_name="thread")
  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  objects = ThreadManager()

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
    # from admin perspective and allowed for premium users
    return bool(self.private.first()) or self.category.is_private

  def get_notification_url(self):
    return self.get_absolute_url()
  def get_notification_message(self):
    return f'{self.post.user.username} you followed has published new thread about ({self.title}) check it now.'

# W: Anyone | R: Anyone
class ThreadPost(models.Model):
  thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread_post')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  sender = GenericRelation(
    NotificationSender,
    object_id_field="sender_id",
    content_type_field="sender_type",
  )

  class Meta:
    verbose_name = 'ThreadPost'
    verbose_name_plural = 'ThreadPosts'

    ordering = ['-created']

  def __str__(self):
    return f'{self.post}'

  def get_notification_url(self):
    return self.post.get_absolute_url()
  def get_notification_message(self):
    return f'New comment from {self.post.user.username} on thread ({self.thread.title}).'

# W: Admin | R: Anyone
class ThreadPin(models.Model):
  thread = models.OneToOneField(Thread, on_delete=models.CASCADE, related_name='pinned')

  objects = ThreadPinManager()

  class Meta:
    verbose_name = 'ThreadPin'
    verbose_name_plural = 'ThreadsPins'

  def __str__(self):
    return f'{self.thread}'




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

