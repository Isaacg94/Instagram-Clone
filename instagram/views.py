from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def feed(request):
    images = Image.newsfeed()
    return render(request, 'timeline.html', {"images":images})