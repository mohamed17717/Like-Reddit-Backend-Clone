import json, os


class NOTIFY_TYPE:
  FOLLOWED = 'followed'
  NEW_THREAD = 'new_thread'
  THREAD_COMMENT = 'thread_comment'
  THREAD_COMMENT = 'thread_comment'
  COMMENT_REPLAY = 'comment_replay'
  POST_UPVOTE = 'post_upvote'
  POST_DOWNVOTE = 'post_downvote'
  POST_EMOJI = 'post_emoji'
  USER_VERIFIED = 'user_verified'
  USER_PREMIUM = 'user_premium'
  USER_BAN = 'user_ban'

  def get_all_types(self) -> list:
    types = []
    for attr in dir(self):
      value = attr == attr.upper() and getattr(self, attr)
      if type(value) == str:
        types.append(value)
    return types

  def get_one_fixture(self, field_value):
    model_name = 'notifications.NotificationType'
    field_name = 'type'
    return { "model": model_name, "fields": { field_name: field_value } }

  def generate_fixture(self) -> str:
    """Generate fixture to set the same values that used in code also in database

      Returns:
          str: json dumped list of dicts as django fixture syntax.
    """

    types = self.get_all_types()
    fixtures = [self.get_one_fixture(t) for t in types]

    return json.dumps(fixtures, indent=2)



fixture_location = os.path.dirname(os.path.abspath(__file__))
fixture_full_path = os.path.join(fixture_location, 'fixtures.json')
with open(fixture_full_path, 'w') as f:
  f.write(NOTIFY_TYPE().generate_fixture())


