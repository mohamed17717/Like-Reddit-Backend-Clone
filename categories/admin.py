from django.contrib import admin

from categories.models import Category, SubCategory

admin.site.register(Category)
admin.site.register(SubCategory)

