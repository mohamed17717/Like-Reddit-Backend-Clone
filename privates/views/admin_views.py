from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from rest_framework.permissions import IsAdminUser

from core.generics import ToggleRecordGenericView

from privates.models import PrivateContent
from threads.models import Thread
from categories.models import Category, SubCategory

class PrivateContent_ToggleThreadPrivate_ApiView(ToggleRecordGenericView):
  model = PrivateContent
  permission_classes = [IsAdminUser]

  def get_queryset_kwargs(self, request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    return {'content_type': ContentType.objects.get_for_model(thread), 'content_id': thread.id}

class PrivateContent_ToggleCategoryPrivate_ApiView(ToggleRecordGenericView):
  model = PrivateContent
  permission_classes = [IsAdminUser]

  def get_queryset_kwargs(self, request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return {'content_type': ContentType.objects.get_for_model(category), 'content_id': category.id}

class PrivateContent_ToggleSubCategoryPrivate_ApiView(ToggleRecordGenericView):
  model = PrivateContent
  permission_classes = [IsAdminUser]

  def get_queryset_kwargs(self, request, sub_category_id):
    sub_category = get_object_or_404(SubCategory, id=sub_category_id)
    return {'content_type': ContentType.objects.get_for_model(sub_category), 'content_id': sub_category.id}

