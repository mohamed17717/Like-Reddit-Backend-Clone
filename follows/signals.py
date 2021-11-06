from django.db.models.signals import post_save
from django.dispatch import receiver

from follows.models import ThreadFollow

# senders
from threads.models import ThreadPost


@receiver(post_save, sender=ThreadPost)
def user_start_follow_thread(sender, instance, created, **kwargs):
  if created:
    thread = instance.thread
    user = instance.post.user

    ThreadFollow.objects.get_or_create(target=thread, follower=user)

