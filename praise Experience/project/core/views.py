from django.shortcuts import render , redirect,get_object_or_404
from item.models import Videos , Artist , Audios 
from . forms import SignupForm , LoginForm 
from django.contrib.auth import logout , login 
from django.contrib.auth.forms import AuthenticationForm





def video(request): 
    watch_id = request.GET.get('watch') 

    if watch_id:
        viewed_videos = request.session.get('viewed_videos',[]) 
        if watch_id not in viewed_videos:
            video = get_object_or_404(Videos,id=watch_id)
            video.views += 1 
            video.save(update_fields=['views']) 
            viewed_videos.append(watch_id)
            request.session['viewed_videos'] = viewed_videos 
    artist = Artist.objects.all()
    videos = Videos.objects.all()[ : 20] 
    return render(request, 'core/videos.html', {
        'artist': artist,
        'videos': videos
    })

def Audio(request):
    audios = Audios.objects.all() 
    return render(request, 'core/Audio.html',{
        'audios' : audios 
    })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # ✅ Pass request here
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('core:index')
    else:
        form = AuthenticationForm(request)  # ✅ Pass request here too
    return render(request, 'core/login.html', {'form': form}) 

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')
    else:
        form = SignupForm()
    
    return render(request, 'core/signup.html', {'form': form})

def index(request):
    watch_id = request.GET.get('watch') 
    if watch_id:
        viewed_videos = request.session.get('viewed_videos',[]) 
        if watch_id not in viewed_videos:
            video = get_object_or_404(Videos,id=watch_id)
            video.views += 1 
            video.save(update_fields=['views']) 
            viewed_videos.append(watch_id)
            request.session['viewed_videos'] = viewed_videos 
    artist = Artist.objects.all() 
    videos = Videos.objects.all() 
    return render(request , 'core/index.html',{
        'artist' : artist,
        'videos' : videos
    })



def logout_view(request):
    logout(request)
    return redirect('core:login')


def about(request): 
    return render(request , 'core/about.html')

def policy(request):
    return render(request , 'core/policy.html')

from django.shortcuts import render

def image_page(request):
    return render(request, 'core/index.html')

# Create your views here.
