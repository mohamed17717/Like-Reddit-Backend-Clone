from django.db.models.expressions import F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from threads.models import Thread
from threads.models import ThreadPost
from follows.models import ThreadFollow
from categories.models import SubCategory

@receiver(post_save, sender=ThreadPost)
def user_start_follow_thread_whenever_commented(sender, instance, created, **kwargs):
  if created:
    thread = instance.thread
    user = instance.post.user

    ThreadFollow.objects.get_or_create(target=thread, follower=user)


@receiver(post_save, sender=Thread)
def increase_threads_counter_in_subcategory(sender, instance, created, **kwargs):
  if created and instance.category:
    SubCategory.objects.select_for_update().filter(pk=instance.category.pk).update(threads_count=F('threads_count') + 1)

@receiver(pre_delete, sender=Thread)
def decrease_threads_counter_in_subcategory(sender, instance, *args, **kwargs):
  if instance.category:
    SubCategory.objects.select_for_update().filter(pk=instance.category.pk).update(threads_count=F('threads_count') - 1)


@receiver(post_save, sender=ThreadPost)
def increase_comments_count_in_thread(sender, instance, created, **kwargs):
  if created:
    Thread.objects.select_for_update().filter(pk=instance.thread.pk).update(comments_count=F('comments_count') + 1)

@receiver(pre_delete, sender=ThreadPost)
def decrease_comments_count_in_thread(sender, instance, *args, **kwargs):
  Thread.objects.select_for_update().filter(pk=instance.thread.pk).update(comments_count=F('comments_count') - 1)

