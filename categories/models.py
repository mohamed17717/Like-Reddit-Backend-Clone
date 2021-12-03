from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from privates.models import PrivateContent


# W: Admin | R: Anyone
class Category(models.Model):
  name = models.CharField(max_length=32)

  # generic field private
  private = GenericRelation(PrivateContent, object_id_field="content_id", related_query_name="category")

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
    return f'{self.id} - {self.name}'

  @property
  def is_private(self):
    return bool(self.private.first())


# W: Admin | R: Anyone
class SubCategory(models.Model):
  name = models.CharField(max_length=32)
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='sub_categories')

  threads_count = models.PositiveIntegerField(default=0)

  # generic field private
  private = GenericRelation(PrivateContent, object_id_field="content_id", related_query_name="subcategory")

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'SubCategory'
    verbose_name_plural = 'SubCategories'

  def __str__(self):
    return f'{self.id} -{self.name} ({self.category.name})'

  @property
  def is_private(self):
    return bool(self.private.first()) or self.category.is_private
