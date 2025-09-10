from django.urls import path
from .import views 

app_name = 'core' 

urlpatterns = [
    path('index/',views.index,name="index"), 
    path('signup/',views.signup_view,name='signup'),
    path('login/', views.login_view, name='login') , 
    path('videos/',views.video,name='video'),
    path('audios/',views.Audio,name='audio'),
    path('logout/',views.logout_view,name='logout'),
    path('about/',views.about,name='about'),
    path('policy/',views.policy,name='policy'),
    path('image/', views.image_page, name='image_page'),
]