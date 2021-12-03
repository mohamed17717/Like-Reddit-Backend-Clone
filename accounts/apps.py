from django.apps import AppConfig

class AccountsConfig(AppConfig):
  name = 'accounts'

  def ready(self):
    import accounts.signals
    import accounts.update_user_model

    return super().ready()
