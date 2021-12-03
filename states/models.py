from django.db import models


class AbstractStateModel(models.Model):
  default_state = None
  states = []

  state = models.CharField(max_length=32)

  class Meta:
    abstract = True

  @classmethod
  def get_default_obj(cls):
    obj = cls.objects.get_or_create(state=cls.default_state)[0].pk
    return obj

  def __str__(self):
    return self.state



# W: Static | R: Admin
class ExistingState(AbstractStateModel):
  default_state = 'active'
  states = ['active', 'soft delete']

  class Meta:
    verbose_name = 'ExistingState'
    verbose_name_plural = 'ExistingState'

  def __str__(self):
    return self.state

  @classmethod
  def get_default_obj(cls):
    obj = cls.objects.get_or_create(state=cls.default_state)[0].pk
    return obj


# W: Static | R: Admin
class PendingState(AbstractStateModel):
  default_state = 'accept'
  states = ['accept', 'pending', 'declined']

  class Meta:
    verbose_name = 'PendingState'
    verbose_name_plural = 'PendingStates'


# W: Static | R: Admin
class PrivacyState(AbstractStateModel):
  default_state = 'public'
  states = ['private', 'public']

  class Meta:
    verbose_name = 'PrivacyState'
    verbose_name_plural = 'PrivacyStates'
