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

  path('dashboard/', admin.site.urls),
  path('docs/', include_docs_urls(title='DJ Forum API'))
]


# from rest_framework.schemas import get_schema_view
# from django.views.generic import TemplateView

# schema_view = get_schema_view(title="DJ Forum API", patterns=urlpatterns)

# urlpatterns += [
#   path('openapi/', schema_view, name='openapi-schema'),
#   path('docs/', TemplateView.as_view(
#     template_name='documentation.html',
#     extra_context={'schema_url':'openapi-schema'}
#   ), name='swagger-ui'),
# ]

