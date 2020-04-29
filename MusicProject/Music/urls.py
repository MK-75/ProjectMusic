from django.urls import path
from Music import views


app_name = 'music'

urlpatterns = [
    path('ArtistSelect/', views.artistSelect, name='artistSelect'),
    path('browse/', views.browse, name='browse'),
    path('radio/', views.radio, name='radio'),

    # CREATE PLAYLIST URLS
    path('MyMusic/', views.myMusic, name='myMusic'),
    path('MyMusic/CreatePlaylist', views.createPlaylist, name="createPlaylist"),
    path('MyMusic/addToFavorites/<int:id>', views.addToFavorites, name="addToFavorites"),
    path('MyMusic/<int:id>', views.deletePlaylist, name='deletePlaylist'),
    path('MyMusic/<str:name>/', views.playlistdetails, name='playlistdetails'),
    path('MyMusic/<str:name>/<int:id>',
         views.playlistSongDelete, name='playlistSongDelete'),
    path('<str:name>/', views.specificAlbum, name='specificAlbum'),
    path('', views.home, name='home')
]
