from django.contrib import admin
from django.urls import path, include


urlpatterns = [
  path('', include('categories.urls', namespace='categories')),
  path('', include('follows.urls', namespace='follows')),

  path('admin/', admin.site.urls),
  path('api-auth/', include('rest_framework.urls'))
]
