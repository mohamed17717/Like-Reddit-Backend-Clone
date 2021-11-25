from django.apps import AppConfig


class ThreadsConfig(AppConfig):
  name = 'threads'

  def ready(self):
    import threads.signals
    return super().ready()
