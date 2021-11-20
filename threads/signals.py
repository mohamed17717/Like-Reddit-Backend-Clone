from django.db.models.expressions import F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from threads.models import Thread
from threads.models import ThreadPost
from follows.models import ThreadFollow


@receiver(post_save, sender=ThreadPost)
def user_start_follow_thread_whenever_commented(sender, instance, created, **kwargs):
  if created:
    thread = instance.thread
    user = instance.post.user

    ThreadFollow.objects.get_or_create(target=thread, follower=user)


@receiver(post_save, sender=Thread)
def increase_threads_counter_in_subcategory(sender, instance, created, **kwargs):
  if created and instance.category:
    instance.category.update(threads_count=F('threads_count') + 1)


@receiver(pre_delete, sender=Thread)
def decrease_threads_counter_in_subcategory(sender, instance, *args, **kwargs):
  if instance.category:
    instance.category.update(threads_count=F('threads_count') - 1)

