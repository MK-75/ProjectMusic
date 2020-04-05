from django.contrib import admin
#from .models import Singer, Album, Song,Favorites,Artist,Images,Playlists,Genre
from .models import Song, Singer, Album, Genre, Playlist, Artist, Favorites
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Favorites)
admin.site.register(Artist)
# admin.site.register(Images)
admin.site.register(Playlist)
admin.site.register(Genre)
