from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def feed(request):
    images = Image.newsfeed()
    return render(request, 'timeline.html', {"images":images})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('feed')

    else:
        form = NewImageForm()
    return render(request, 'upload.html', {"form": form})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    title = "Profile"
    profile = User.objects.get(username=username)
    users = User.objects.get(username=username)
    try :
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)


    return render(request, 'profile.html', {'title':title,'profile':profile, 'profile_details':profile_details})

