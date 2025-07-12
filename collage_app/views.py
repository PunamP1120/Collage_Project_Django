from django.shortcuts import render, redirect
from .forms import CollageForm
from .models import Collage, ImageItem

def upload_view(request):
    if request.method == 'POST':
        form = CollageForm(request.POST, request.FILES)
        if form.is_valid():
            collage = Collage.objects.create(title=form.cleaned_data['title'])
            images = form.cleaned_data['images']
            for image in images:
                ImageItem.objects.create(collage=collage, image=image)
            return redirect('display_collage', collage_id=collage.id)
    else:
        form = CollageForm()
    return render(request, 'collage_app/upload.html', {'form': form})

def display_view(request, collage_id):
    collage = Collage.objects.get(id=collage_id)
    return render(request, 'collage_app/display.html', {'collage': collage})

def list_view(request):
    collages = Collage.objects.all().order_by('-created_at')
    return render(request, 'collage_app/list.html', {'collages': collages})