from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Image, Location

# Create your views here.
def index(request):
    title = 'Home'
    images = Image.get_all_images()
    locations = Location.objects.all()
    print(images)
    return render(request, 'index.html', {'title':title, 'images':images, 'locations':locations})

def single_image(request, image_id):
    title = f'{image_id}'

    return render(request,'single_image.html',{'title':title})