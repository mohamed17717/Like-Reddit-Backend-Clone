from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.query_utils import Q
from django.db.models.signals import post_save
from django.dispatch import receiver

from notifications.models import Notification, NotificationSender, NotificationType

from notifications.static_vals import NOTIFY_TYPE as N_Type

# senders
from follows.models import UserFollow
from posts.models import PostReplay
from threads.models import Thread, ThreadPost
from impressions.models import PostDownVote, PostEmoji, PostUpVote
from accounts.models import UserBan, UserPremium, UserVerified


# TODO
#   maybe set unfollowed signal
#   notification seen flag
#   signal for pinned thread
#   signal for pending thread accepted or declined
#   signal for removed thread or hidden



User = get_user_model()

def notify(user:User, n_type:str, sender:models.Model):
  type_obj, _ = NotificationType.objects.get_or_create(type=n_type)
  sender_obj = NotificationSender.objects.create(sender_object=sender)

  Notification.objects.create(user=user, type=type_obj, sender=sender_obj)


def notify_many(users:list[User], n_type:str, sender:models.Model):
  type_obj, _ = NotificationType.objects.get_or_create(type=n_type)
  sender_obj = NotificationSender.objects.create(sender_object=sender)

  notifications = []
  for user in users:
    notifications.append(
      Notification(user=user, type=type_obj, sender=sender_obj)
    )

  Notification.objects.bulk_create(notifications)



@receiver(post_save, sender=UserFollow)
def notify_user_for_getting_followed(sender, instance, created, **kwargs):
  if created:
    user = instance.target
    notify(user, N_Type.FOLLOWED, instance)


@receiver(post_save, sender=Thread)
def notify_user_followers_for_publishing_new_thread(sender, instance, created, **kwargs):
  if created:
    publisher = instance.post.user
    followers = [item.follower for item in publisher.user_followers.all()]

    notify_many(followers, N_Type.NEW_THREAD, instance)


@receiver(post_save, sender=ThreadPost)
def notify_user_for_someone_commented_on_his_thread(sender, instance, created, **kwargs):
  if created:
    thread_publisher = instance.thread.post.user
    notify(thread_publisher, N_Type.THREAD_COMMENT, instance)


@receiver(post_save, sender=ThreadPost)
def notify_thread_followers_for_new_comment(sender, instance, created, **kwargs):
  if created:
    comment_publisher = instance.post.user

    thread_followers = instance.thread.thread_followers.filter(~Q(follower=comment_publisher))
    followers = [item.follower for item in thread_followers]

    notify_many(followers, N_Type.THREAD_COMMENT, instance)


@receiver(post_save, sender=PostReplay)
def notify_user_for_somone_replaying_to_his_comment(sender, instance, created, **kwargs):
  if created:
    user = instance.post.user
    notify(user, N_Type.COMMENT_REPLAY, instance)



@receiver(post_save, sender=PostUpVote)
def notify_user_for_upvote(sender, instance, created, **kwargs):
  if created:
    user = instance.post.user
    notify(user, N_Type.POST_UPVOTE, instance)


@receiver(post_save, sender=PostDownVote)
def notify_user_for_downvote(sender, instance, created, **kwargs):
  if created:
    user = instance.post.user
    notify(user, N_Type.POST_DOWNVOTE, instance)


@receiver(post_save, sender=PostEmoji)
def notify_user_for_emoji(sender, instance, created, **kwargs):
  if created:
    user = instance.post.user
    notify(user, N_Type.POST_EMOJI, instance)


@receiver(post_save, sender=UserVerified)
def notify_user_for_getting_verified(sender, instance, created, **kwargs):
  if created:
    user = instance.user
    notify(user, N_Type.USER_VERIFIED, instance)


@receiver(post_save, sender=UserPremium)
def notify_user_for_getting_premium(sender, instance, created, **kwargs):
  if created:
    user = instance.user
    notify(user, N_Type.USER_PREMIUM, instance)


@receiver(post_save, sender=UserBan)
def notify_user_for_getting_ban(sender, instance, created, **kwargs):
  if created:
    user = instance.user
    notify(user, N_Type.USER_BAN, instance)


