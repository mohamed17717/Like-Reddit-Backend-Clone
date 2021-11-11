from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls


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
  path('', include('posts.urls', namespace='posts')),

  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls')),
  path('auth/', include('djoser.urls')),
  path('auth/', include('djoser.urls.jwt')),
  path('docs/', include_docs_urls(title='Snippet API'))
]
