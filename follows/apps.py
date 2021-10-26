from django.apps import AppConfig


class FollowsConfig(AppConfig):
  default_auto_field = 'django.db.models.BigAutoField'
  name = 'follows'

  def ready(self):
    import follows.signals
    return super().ready()
