# swift_transfer/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional user-related fields if needed

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=255, default='Title')
    num_images = models.IntegerField(default=0)
    num_anchor_images = models.IntegerField(default=0)
    message = models.TextField(default='Message')
    uploaded_at = models.DateTimeField(auto_now_add=True)
