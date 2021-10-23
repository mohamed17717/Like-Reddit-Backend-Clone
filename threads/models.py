from django.db import models

from posts.models import Post
from categories.models import SubCategory


# TODO:
#   set counters for threads etc...


# W: Static | R: Admin
class ThreadStates(models.Model):
  state = models.CharField(max_length=32)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.name


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

  @classmethod
  def get_pending_obj(cls): return cls.get_value_obj('pending')

  @classmethod
  def get_pinned_obj(cls): return cls.get_value_obj('pinned')


# W: Anyone | R: Anyone
class Thread(models.Model):
  post = models.OneToOneField(Post, on_delete=models.CASCADE, related_name='thread')
  title = models.CharField(max_length=128)
  category = models.ForeignKey(SubCategory, on_delete=models.PROTECT, related_name='threads')
  state = models.ForeignKey(ThreadStates, on_delete=models.SET_DEFAULT, default=ThreadStates.get_active_obj, related_name='threads')

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'Thread'
    verbose_name_plural = 'Threads'

  def __str__(self):
    return self.title

