from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey



# W: Runtime | R: Runtime
class PrivateContent(models.Model):
  'Thread or Category or SubCategory'
  content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
  content_id = models.PositiveIntegerField()
  content_object = GenericForeignKey('content_type', 'content_id')

  class Meta:
    verbose_name = 'PrivateContent'
    verbose_name_plural = 'PrivateContents'

  def __str__(self):
    return self.content_object

