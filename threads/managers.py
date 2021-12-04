from django.db import models
from django.db.models.expressions import F
from django.shortcuts import get_object_or_404


class ThreadQuerySet(models.QuerySet):
  def all_alive(self):
    qs = self.filter(**self.alive_conditions)
    return qs

  def one_alive(self, **kwargs):
    obj = get_object_or_404(self.model, **self.alive_conditions, **kwargs)
    return obj
  
  def all_for_owner(self, user):
    qs = self.filter(post__user=user, **self.exist_condition)
    return qs
  
  def one_for_owner(self, user, **kwargs):
    obj = get_object_or_404(self.model, **self.exist_condition, post__user=user, **kwargs)
    return obj

  @property
  def alive_conditions(self):
    return {
      **self.exist_condition,
      'pending_state__state': 'accept', 
      'privacy_state__state': 'public',
    }
  @property
  def exist_condition(self):
    return { 'post__existing_state__state': 'active', }


class ThreadManager(models.Manager):
  def get_queryset(self):
    return ThreadQuerySet(self.model, using=self._db, hints=self._hints)

  def all_alive(self):
    return self.get_queryset().all_alive()

  def one_alive(self, **kwargs):
    return self.get_queryset().one_alive(**kwargs)

  def all_for_owner(self, user):
    return self.get_queryset().all_for_owner(user)

  def one_for_owner(self, user, **kwargs):
    return self.get_queryset().one_for_owner(user, **kwargs)

  @property
  def alive_conditions(self):
    return self.get_queryset().alive_conditions
  @property
  def exist_condition(self):
    return self.get_queryset().exist_condition

