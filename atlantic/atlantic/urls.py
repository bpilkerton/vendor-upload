from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('upload.urls')),
    path('upload/', admin.site.urls),
]
