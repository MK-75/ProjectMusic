from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def addToFavorites(request, id):
    flag = False
    s = Song.objects.get(id=id)
    song = Song.objects.all()
    favorite = Favorites.objects.all()
    current_user = request.user
    for fav in favorite:
        if fav.song_id == id :
            fav.delete()
            flag = True
    
    if flag == False :
        f = Favorites(song=s, user=current_user)
        f.save()
    
    f = []
    f = Favorites.objects.all()
    context = {'f': f, 'song':song}
    return render(request, 'music/addToFavorites.html', context)

def playlistSongDelete(request, name, id):
    playlist = Playlist.objects.get(playlist_name=name)
    song = playlist.songs.all()
    song_to_delete = song.get(id=id)
    playlist.songs.remove(song_to_delete)
    context = {'playlist': playlist}
    return HttpResponseRedirect(reverse('music:playlistdetails', kwargs={'name': playlist.playlist_name}))


def playlistdetails(request, name):
    playlist = Playlist.objects.get(playlist_name=name)
    context = {'playlist': playlist}
    return render(request, 'music/albumDetails.html', context)


def myMusic(request):
    songs = Song.objects.all()
    current_user = request.user
    playlist = Playlist.objects.filter(user=current_user)
    context = {'songs': songs, 'playlist': playlist}
    return render(request, 'music/myMusic.html', context)


def deletePlaylist(request, id):
    playlist = Playlist.objects.get(id=id)
    playlist.delete()
    p = Playlist.objects.all()
    context = {'p': p}
    return HttpResponseRedirect(reverse('music:myMusic'))


@login_required
def createPlaylist(request):
    songs = Song.objects.all()
    context = {'songs': songs}
    if request.method == "POST":
        my_name = request.POST['playlistName']
        my_songs = request.POST.getlist('songList')
        current_user = request.user
        playlist = Playlist.objects.create(
            user=current_user, playlist_name=my_name)
        for name in my_songs:
            selectedSong = Song.objects.get(songName=name)
            playlist.songs.add(selectedSong)
        return HttpResponseRedirect(reverse('music:myMusic'))

    return render(request, 'music/createPlaylist.html', context)


def browse(request):
    return render(request, 'music/browse.html')


def radio(request):
    singer = Singer.objects.all()
    context = {'singer': singer}
    return render(request, 'music/radio.html', context)
