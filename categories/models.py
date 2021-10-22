from django.db import models


class Category(models.Model):
  title = models.CharField(max_length=128)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.title


class SubCategory(models.Model):
  title = models.CharField(max_length=128)
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='sub_categories')

  class Meta:
    verbose_name = 'SubCategory'
    verbose_name_plural = 'SubCategories'

  def __str__(self):
    return f'{self.title} ({self.category.title})'

