from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()

# TODO: 
  #   Signal in ban table for the user depend on PostReport update decision
  #


# W: No | R: Admin
class ReportDecision(models.Model):
  name = models.CharField(max_length=32)

  class Meta:
    verbose_name = 'ReportDecision'
    verbose_name_plural = 'ReportDecisions'

  def __str__(self):
    return self.name

  @classmethod
  def get_default_value(cls) -> int:
    return cls.objects.get_or_create(name='pending')[0].pk

# W: Admin | R: Anyone
class ReportType(models.Model):
  """ 2 Layers of report (1) type like cant be here (2) its nudity """
  title = models.CharField(max_length=256)
  description = models.TextField(blank=True, null=True)

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'ReportType'
    verbose_name_plural = 'ReportTypes'

  def __str__(self):
    return self.title

# W: Admin | R: Anyone
class ReportSubType(models.Model):
  title = models.CharField(max_length=256)
  type = models.ForeignKey(ReportType, on_delete=models.PROTECT, related_name='sub_types')
  description = models.TextField(blank=True, null=True)

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'ReportSubType'
    verbose_name_plural = 'ReportSubTypes'

  def __str__(self):
    return self.title

# W: Anyone | R: Admin
class PostReport(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reports')
  type = models.ForeignKey(ReportSubType, on_delete=models.SET_NULL, related_name='reports', blank=True, null=True)
  decision = models.ForeignKey(ReportDecision, on_delete=models.SET_DEFAULT, default=ReportDecision.get_default_value)

  created = models.DateField(auto_now_add=True)
  updated = models.DateField(auto_now=True)

  class Meta:
    verbose_name = 'PostReport'
    verbose_name_plural = 'PostReports'

    ordering = ['-created']

  def __str__(self):
    return f'Post: {self.post.pk} ({self.type.title})'
