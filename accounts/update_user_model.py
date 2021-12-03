from django.contrib.auth import get_user_model
import datetime as dt

from accounts.models import UserBan


@property
def is_premium(self):
  try:
    self.premium
    check = True
  except:
    check = False
  return check

@property
def is_banned(self):
  bans = self.bans.all().filter(state='active')

  ban_state = False
  ended_bans = []

  for ban in bans:
    days = dt.timedelta(days=ban.days)
    is_active = ban.start + days > dt.datetime.now()
    if is_active:
      ban_state = True
      break

    ban.state = 'soft delete'
    ended_bans.append(ban)

  UserBan.objects.select_for_update().bulk_update(ended_bans, fields=['state'])
  return ban_state



User = get_user_model()

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False
User.USERNAME_FIELD = 'email'
User.REQUIRED_FIELDS = ['username']

User.add_to_class('is_premium', is_premium)
User.add_to_class('is_banned', is_banned)
