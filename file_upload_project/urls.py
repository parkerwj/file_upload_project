"""
URL configuration for file_upload_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# file_upload_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from swift_transfer.views import profile, upload_file, file_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('swift_transfer.urls')),
    # Use Django's built-in LoginView for login
    path('login/', LoginView.as_view(), name='login'),
    # Use Django's built-in LogoutView for logout
    path('logout/', LogoutView.as_view(), name='logout'),
    # Profile view
    path('accounts/profile/', profile, name='profile'),
    path('file_list/', file_list, name='file_list'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    # In production, you would typically use a web server to serve media files
    # For development purposes, serve media files directly by Django
    from django.views.static import serve
    urlpatterns += [
        path('media/<path>', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
