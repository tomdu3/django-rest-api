from django.contrib import admin
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('silk/', include('silk.urls', namespace='silk')),
]

