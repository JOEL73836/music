from django.urls import path
from .import views

app_name = 'item'

urlpatterns = [
    path('artist/<int:artist_id>/', views.artist_videos, name='artist_videos') 
]