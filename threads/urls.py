from django.urls import path

from threads.views import (
  index
)

app_name = 'threads'

urlpatterns = [
  path('thread/<int:pk>/', index, name="thread-retrieve"),
]
