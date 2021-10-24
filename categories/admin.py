from django.contrib import admin

from .models import Category
from .models import SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)

