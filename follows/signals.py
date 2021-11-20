from django.db.models.expressions import F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from follows.models import ThreadFollow

# senders
from threads.models import ThreadPost
from follows.models import UserFollow


@receiver(post_save, sender=ThreadPost)
def user_start_follow_thread(sender, instance, created, **kwargs):
  if created:
    thread = instance.thread
    user = instance.post.user

    ThreadFollow.objects.get_or_create(target=thread, follower=user)


@receiver(post_save, sender=UserFollow)
def increase_follow_counter_in_profile(sender, instance, created, **kwargs):
  if created:
    target = instance.target
    follower = instance.follower

    follower.profile.update(following_count=F('following_count') + 1)
    target.profile.update(follower_count=F('follower_count') + 1)


@receiver(pre_delete, sender=UserFollow)
def decrease_follow_counter_in_profile(sender, instance, *args, **kwargs):
  target = instance.target
  follower = instance.follower

  follower.profile.update(following_count=F('following_count') - 1)
  target.profile.update(follower_count=F('follower_count') - 1)

