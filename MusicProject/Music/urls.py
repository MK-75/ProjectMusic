from django.urls import path
from Music import views


app_name = 'music'

urlpatterns = [
    path('ArtistSelect/', views.artistSelect, name='artistSelect'),
    path('browse/', views.browse, name='browse'),
    path('radio/', views.radio, name='radio'),
    path('MyMusic/', views.myMusic, name='myMusic'),
    path('MyMusic/CreatePlaylist', views.createPlaylist, name="createPlaylist"),
    path('<str:name>/', views.specificAlbum, name='specificAlbum'),
    path('MyMusic/<str:name>/', views.playlistdetails, name='playlistdetails'),
    path('MyMusic/<str:name>/', views.deletePlaylist, name='deletePlaylist'),

    path('', views.home, name='home')
]
