from django.contrib import admin
from django.urls import path

from sandbox import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getHashOfFile/', views.getHashOfFile, name='api_hash'),
    path('api/files/', views.FileHashList.as_view(), name='file-hash-list'),
    path('api/checkIfFileExists/', views.checkIfFileExists, name='api_check')
]
