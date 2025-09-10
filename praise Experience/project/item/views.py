from django.shortcuts import render , get_object_or_404

from .models import Videos , Artist 

def artist_videos(request, artist_id, video_id=None):
    watch_id = request.GET.get('watch') 

    if watch_id:
        viewed_videos = request.session.get('viewed_videos',[]) 
        if watch_id not in viewed_videos:
            video = get_object_or_404(Videos,id=watch_id)
            video.views += 1 
            video.save(update_fields=['views']) 
            viewed_videos.append(watch_id)
            request.session['viewed_videos'] = viewed_videos 

    artist = get_object_or_404(Artist, pk=artist_id)
    
    if video_id:
        # You can optionally fetch the video here if needed
        video = get_object_or_404(Videos, pk=video_id, artist=artist)
    
    videos = Videos.objects.filter(artist=artist)
    
    return render(request, 'item/artist_videos.html', {
        'artist': artist,
        'videos': videos,
    })




# Create your views here.
