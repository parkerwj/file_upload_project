# swift_transfer/forms.py
from django import forms
from .models import UploadedFile

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file','title','num_images','num_anchor_images','message']
