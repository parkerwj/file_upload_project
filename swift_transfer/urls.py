# file_upload_project/urls.py
from django.contrib import admin
from django.urls import path, include
from swift_transfer.views import home, upload_file, UploadedFileListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('upload/', upload_file, name='upload_file'),
    path('files/', UploadedFileListView.as_view(), name='file-list'),
    # Add more paths as needed
]
