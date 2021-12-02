from django.apps import AppConfig

from django.contrib.auth import get_user_model


class AccountsConfig(AppConfig):
  name = 'accounts'

  def ready(self):
    import accounts.signals
    
    User = get_user_model()

    @property
    def is_premium(self):
      try:
        self.premium
        check = True
      except:
        check = False
      return check

    User._meta.get_field('email')._unique = True
    User._meta.get_field('email').blank = False
    User._meta.get_field('email').null = False
    User.USERNAME_FIELD = 'email'
    User.REQUIRED_FIELDS = ['username']

    User.add_to_class('is_premium', is_premium)

    return super().ready()
