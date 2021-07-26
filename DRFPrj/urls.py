from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api_urls import router




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('api-auth/',include('rest_framework.urls')),
]
