# swift_transfer/views.py
from django.shortcuts import render, redirect
from .models import UserProfile, UploadedFile
from .forms import FileUploadForm

def home(request):
    # Add logic to display user-specific content
    return render(request, 'swift_transfer/home.html')

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'swift_transfer/upload_file.html', {'form': form})

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    # Your profile view logic here
    return render(request, 'profile.html')

@login_required
def file_list(request):
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'file_list.html', {'files': files})