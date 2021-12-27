from django.db import models
from django.db.models.expressions import F
from django.shortcuts import get_object_or_404

import threads.models as thModels
import posts.models as pModels
from states.models import ExistingState

class PostQuerySet(models.QuerySet):
  def create_comment_on_thread(self, comment, thread):
    obj = thModels.ThreadPost.objects.create(thread=thread, post=comment)
    return obj

  def create_replay_on_comment(self, replay, comment):
    pModels.PostReplay.objects.create(post=comment, replay=replay)
    return replay
  
  def create_deep(self, data):
    # data = {user: user, post_content: {type: {type: ''}, content: ''}, }
    post_content_data = data.pop('post_content')

    post_content_type_data = post_content_data.pop('type')
    if post_content_type_data:
      post_content_data['type'] = get_object_or_404(pModels.PostConetntType, **post_content_type_data)

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

      content_type = post_content_data.get('type', oc_post_content.type.type)
      content_type = content_type if type(content_type) == str else content_type['type']
      oc_post_content.type = get_object_or_404(pModels.PostConetntType, type=content_type)

      oc_post_content.save()

    if description_data:
      post_instance.description = description_data
      post_instance.save()

    if state_data:
      new_state = get_object_or_404(ExistingState, **state_data)
      post_instance.state = new_state
      post_instance.save()

    return post_instance

  def update_counter_field(self, pk, field_name, amount):
    new_value = { field_name: F(field_name) + amount }
    self.select_for_update().filter(pk=pk).update(**new_value)

  def all_alive(self):
    qs = self.filter(**self.exist_condition)
    return qs

  def one_alive(self, **kwargs):
    obj = get_object_or_404(self.model, **self.exist_condition, **kwargs)
    return obj

  def all_for_owner(self, user):
    qs = self.filter(user=user, **self.exist_condition)
    return qs

  @property
  def exist_condition(self):
    return {'existing_state__state': 'active'}

class PostManager(models.Manager):
  def get_queryset(self):
    return PostQuerySet(self.model, using=self._db, hints=self._hints)

  def create_replay_on_comment(self, replay, comment):
    return self.get_queryset().create_replay_on_comment(replay, comment)

  def create_comment_on_thread(self, comment, thread):
    return self.get_queryset().create_comment_on_thread(comment, thread)


  def create_deep(self, data):
    return self.get_queryset().create_deep(data)

  def update_deep(self, post_instance, post_data):
    return self.get_queryset().update_deep(post_instance, post_data)

  def update_counter_field(self, pk, field_name, amount):
    return self.get_queryset().update_counter_field(pk, field_name, amount)


  def all_alive(self):
    return self.get_queryset().all_alive()

  def one_alive(self, **kwargs):
    return self.get_queryset().one_alive(**kwargs)

  def all_for_owner(self, user):
    return self.get_queryset().all_for_owner(user)
