from django.db.models.expressions import F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from threads.models import Thread



@receiver(post_save, sender=Thread)
def increase_threads_counter_in_subcategory(sender, instance, created, **kwargs):
  if created and instance.category:
    instance.category.update(threads_count=F('threads_count') + 1)


@receiver(pre_delete, sender=Thread)
def decrease_threads_counter_in_subcategory(sender, instance, *args, **kwargs):
  if instance.category:
    instance.category.update(threads_count=F('threads_count') - 1)

