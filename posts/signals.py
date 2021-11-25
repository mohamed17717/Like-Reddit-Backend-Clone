from django.db.models.signals import post_save, pre_delete

from impressions.models import PostUpVote, PostDownVote, PostEmoji
from posts.models import Post, PostReplay


def increase(field_name):
  def func(sender, instance, created, **kwargs):
    if created:
      Post.objects.update_counter_field(instance.post.pk, field_name, 1)
  return func

def decrease(field_name):
  def func(sender, instance, *args, **kwargs):
    Post.objects.update_counter_field(instance.post.pk, field_name, -1)
  return func


post_save.connect(increase('upvote_count'), sender=PostUpVote)
pre_delete.connect(decrease('upvote_count'), sender=PostUpVote)

post_save.connect(increase('downvote_count'), sender=PostDownVote)
pre_delete.connect(decrease('downvote_count'), sender=PostDownVote)

post_save.connect(increase('emoji_count'), sender=PostEmoji)
pre_delete.connect(decrease('emoji_count'), sender=PostEmoji)

post_save.connect(increase('replays_count'), sender=PostReplay)
pre_delete.connect(decrease('replays_count'), sender=PostReplay)

