from django.db.models.expressions import F
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from follows.models import UserFollow
from accounts.models import UserProfile

@receiver(post_save, sender=UserFollow)
def increase_follow_counter_in_profile(sender, instance, created, **kwargs):
  if created:
    target = instance.target
    follower = instance.follower

    UserProfile.objects.select_for_update().filter(pk=target.pk).update(follower_count=F('follower_count') + 1)
    UserProfile.objects.select_for_update().filter(pk=follower.pk).update(following_count=F('following_count') + 1)

@receiver(pre_delete, sender=UserFollow)
def decrease_follow_counter_in_profile(sender, instance, *args, **kwargs):
  target = instance.target
  follower = instance.follower

  UserProfile.objects.select_for_update().filter(pk=target.pk).update(follower_count=F('follower_count') - 1)
  UserProfile.objects.select_for_update().filter(pk=follower.pk).update(following_count=F('following_count') - 1)

