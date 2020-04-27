from django.shortcuts import render
from django.http import HttpResponse
from Music.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    album = Album.objects.all()
    context = {'album': album}
    return render(request, 'music/home.html', context)


def artistSelect(request):
    return render(request, 'music/bollyselect.html')


def specificAlbum(request, name):
    album = Album.objects.get(album_name=name)
    songs = []
    sng = album.song_set.all()
    for s in sng:
        songs.append(s.song_path)

    context = {'album': album, 'songs': songs}
    return render(request, 'music/album.html', context)

def playlistdetails(request,name):
    playlist=Playlist.objects.get(playlist_name=name)
   
    context = {'playlist':playlist}
    return render(request, 'music/albumDetails.html', context)

    
def myMusic(request):
    songs = Song.objects.all()
    current_user=request.user
    playlist=Playlist.objects.filter(user=current_user)
    context = {'songs': songs,'playlist':playlist}
    return render(request, 'music/myMusic.html', context)

def deletePlaylist(request,name):
    playlist=Playlist.objects.get(playlist_name=name)
    playlist.delete()
    p=Playlist.objects.all() 
    context = {'p':p}
    return render(request,'music/myMusic.html',context)






@login_required
def createPlaylist(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    if request.method == "POST":
        # my_id = my_id + 1
        my_name = request.POST['playlistName']
        my_songs = request.POST.getlist('songList')
        current_user = request.user
        playlist = Playlist.objects.create(user=current_user, playlist_name=my_name)
        for name in my_songs:
            selectedSong = Song.objects.get(songName=name)
            playlist.songs.add(selectedSong)

        # my_s = request.POST.get('song_name', '')
        # my_songs = Song.objects.get(songName=my_s)
        # my_name = request.POST('playlistName')
        # current_user = request.user
        # playlist = Playlist(id=1, user=current_user,
        #                     playlist_name=my_name)
        # playlist.songs.add(my_songs)
        # playlist.save()
        # return HttpResponse(my_songs)

    return render(request, 'music/createPlaylist.html', context)


def browse(request):
    return render(request, 'music/browse.html')


def radio(request):
    singer = Singer.objects.all()
    context = {'singer': singer}
    return render(request, 'music/radio.html', context)
