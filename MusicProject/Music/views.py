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


def myMusic(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    return render(request, 'music/myMusic.html', context)


@login_required
def createPlaylist(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    if request.method == "POST":
        my_s = request.POST.get('song_name', '')
        my_songs = Song.objects.get(songName=my_s)
        my_name = request.POST('playlistName')
        current_user = request.user
        playlist = Playlist(id=1, user=current_user,
                            playlist_name=my_name)
        playlist.songs.add(my_songs)
        playlist.save()
        return HttpResponse('Your playlist is successfully created')

    return render(request, 'music/createPlaylist.html', context)


def browse(request):
    return render(request, 'music/browse.html')


def radio(request):
    singer = Singer.objects.all()
    context = {'singer': singer}
    return render(request, 'music/radio.html',context)
