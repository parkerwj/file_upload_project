# file_upload_project/urls.py
from django.contrib import admin
from django.urls import path, include
from swift_transfer.views import home, upload_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('upload/', upload_file, name='upload_file'),
    # Add more paths as needed
]
