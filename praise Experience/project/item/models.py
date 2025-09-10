from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model): 
    name = models.CharField(max_length=255) 

    def __str__(self):
        return self.name 

class Videos(models.Model):
    artist = models.ForeignKey(Artist,related_name='item', on_delete=models.CASCADE)
    title = models.CharField(max_length=255) 
    cover_image = models.ImageField(upload_to='image',blank=True,null=True) 
    videos = models.FileField(upload_to='videos',blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveBigIntegerField(default=0) 

    def __str__(self):
        return self.title 
    
class Audios(models.Model): 
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=255) 
    Audio = models.FileField(upload_to='Audios',blank=True,null=True) 
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title
    
class VideoView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'video')



# Create your models here.
