from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



# W: Runtime | R: Runtime
class PrivateContent(models.Model):
  limits = models.Q(app_label='threads', model='Thread') | \
    models.Q(app_label='categories', model='Category') | \
    models.Q(app_label='categories', model='SubCategory')

  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to=limits)
  content_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'content_id')

  class Meta:
    verbose_name = 'PrivateContent'
    verbose_name_plural = 'PrivateContents'

    constraints = [
      models.UniqueConstraint(fields=['content_type', 'content_id'], name='set_private_only_once')
    ]

  def __str__(self):
    return f'{self.content_object}'

