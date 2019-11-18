from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image
from django.contrib.auth.decorators import login_required.

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def feed(request):
    images = Image.newsfeed()
    return render(request, 'timeline.html', {"images":images})