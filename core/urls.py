from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path(
        'api/v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
        ),
    path(
        'api/v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
        ),
    path('silk/', include('silk.urls', namespace='silk')),
    # API schema generation
     path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path(
        'api/schema/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
        ),
    path(
        'api/schema/redoc/', 
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
        ),
]

