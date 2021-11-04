from django.contrib import admin
from django.urls import path, include


urlpatterns = [
  path('', include('categories.urls', namespace='categories')),
  path('', include('follows.urls', namespace='follows')),
  path('', include('notifications.urls', namespace='notifications')),
  path('', include('privates.urls', namespace='privates')),
  path('', include('saves.urls', namespace='saves')),
  path('', include('threads.urls', namespace='threads')),
  path('', include('rewards.urls', namespace='rewards')),
  path('', include('reports.urls', namespace='reports')),
  path('', include('impressions.urls', namespace='impressions')),
  path('', include('accounts.urls', namespace='accounts')),

  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls'))
]
