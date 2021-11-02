from django.urls import path
from notifications.views import Notification_ListOwn_ApiView

app_name = 'notifications'

urlpatterns = [
  path('notifications/', Notification_ListOwn_ApiView.as_view(), name='list-notifications'),
]

