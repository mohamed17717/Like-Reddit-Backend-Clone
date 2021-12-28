from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType

from rest_framework.permissions import IsAdminUser

from core.generics import ToggleRecordGenericView

from privates.models import PrivateContent
from threads.models import Thread
from categories.models import Category, SubCategory


class Abstract_PrivateContent_ApiView(ToggleRecordGenericView):
  model = PrivateContent
  permission_classes = [IsAdminUser]

  related_model = None # required
  lookup_url_kwarg = None # required

  def get_queryset_kwargs(self, request, **kwargs):
    item_id = kwargs.get(self.lookup_url_kwarg)
    thread = get_object_or_404(self.related_model, id=item_id)
    return {'content_type': ContentType.objects.get_for_model(thread), 'content_id': thread.id}


class PrivateContent_ToggleThreadPrivate_ApiView(Abstract_PrivateContent_ApiView):
  related_model = Thread
  lookup_url_kwarg = 'thread_id'
class PrivateContent_ToggleCategoryPrivate_ApiView(Abstract_PrivateContent_ApiView):
  related_model = Category
  lookup_url_kwarg = 'category_id'
class PrivateContent_ToggleSubCategoryPrivate_ApiView(Abstract_PrivateContent_ApiView):
  related_model = SubCategory
  lookup_url_kwarg = 'sub_category_id'
