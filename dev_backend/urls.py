from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev_app/', include('dev_app.urls')),  # API 경로 추가
]
