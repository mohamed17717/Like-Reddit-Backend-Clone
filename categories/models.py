from django.db import models


# W: Admin | R: Anyone
class Category(models.Model):
  name = models.CharField(max_length=32)

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __str__(self):
    return f'{self.id} - {self.name}'


# W: Admin | R: Anyone
class SubCategory(models.Model):
  name = models.CharField(max_length=32)
  category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='sub_categories')

  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name = 'SubCategory'
    verbose_name_plural = 'SubCategories'

  def __str__(self):
    return f'{self.id} -{self.name} ({self.category.name})'

