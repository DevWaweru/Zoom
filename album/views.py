from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    print(images)
    return render(request, 'index.html', {'title':title, 'images':images})

def single_image(request, image_id):
    title = f'{image_id}'

    return render(request,'single_image.html',{'title':title})