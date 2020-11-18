from django.contrib import admin
from django.urls import path, include

from whiskys.urls import router

urlpatterns = [
    path('api/v1/', include('whiskys.urls')),
    path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('authentication/', include('rest_framework.urls')),
]
