from django.db import models
from django.shortcuts import get_object_or_404

import threads.models as thModels
import posts.models as pModels


class PostQuerySet(models.QuerySet):
  def create_comment_on_thread(self, user, thread, post_data):
    post = self.create_deep({'user': user, **post_data})
    obj = thModels.ThreadPost.objects.create(thread=thread, post=post)

    return obj

  def create_replay_on_comment(self, user, comment_id, post_data):
    comment = get_object_or_404(self.model, id=comment_id)
    replay = self.create_deep({'user': user, **post_data})

    pModels.PostReplay.objects.create(post=comment, replay=replay)
    return replay
  
  def create_deep(self, data):
    # data = {user: user, post_content: {type: {type: ''}, content: ''}, }
    post_content_data = data.pop('post_content')

    post_content_type_data = post_content_data.pop('type')
    if post_content_type_data:
      post_content_data['type'] = get_object_or_404(pModels.PostContentType, **post_content_type_data)

    data['post_content'] = pModels.PostContent.objects.create(**post_content_data)

    post = self.create(**data)
    return post

  def update_deep(self, post_instance, post_data):
    post_content_data = post_data.get('post_content')
    description_data = post_data.get('description')
    state_data = post_data.get('state')

    if post_content_data:
      oc_post_content = post_instance.post_content

      oc_post_content.content = post_content_data.get('content', oc_post_content.content)

      content_type = post_content_data.get('type', '')
      content_type = content_type if type(content_type) == str else content_type['type']
      oc_post_content.type = get_object_or_404(pModels.PostContentType, type=content_type)

      oc_post_content.save()

    if description_data:
      post_instance.description = description_data
      post_instance.save()

    if state_data:
      new_state = get_object_or_404(pModels.PostState, **state_data)
      post_instance.state = new_state
      post_instance.save()

    return post_instance

class PostManager(models.Manager):
  def get_queryset(self):
    return PostQuerySet(self.model, using=self._db, hints=self._hints)

  def create_replay_on_comment(self, user, comment_id, post_data):
    return self.get_queryset().create_replay_on_comment(user, comment_id, post_data)

  def create_comment_on_thread(self, user, thread, post_data):
    return self.get_queryset().create_comment_on_thread(user, thread, post_data)


  def create_deep(self, data):
    return self.get_queryset().create_deep(data)

  def update_deep(self, post_instance, post_data):
    return self.get_queryset().update_deep(post_instance, post_data)
