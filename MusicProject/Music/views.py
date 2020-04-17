from django.shortcuts import render
from django.http import HttpResponse
from Music.models import *

# Create your views here.


def home(request):
    album = Album.objects.all()
    context = {'album': album}
    return render(request, 'music/home.html', context)


# def index(request):
#     # return HttpResponse('This is the landing page')
#     return render(request, 'index.html')

def specificAlbum(request,name):
    album = Album.objects.get(album_name=name)
    songs=Song.objects.all()
    context = {'album': album,'songs':songs}
    return render(request, 'music/album.html', context)


def browse(request):
    return render(request, 'music/browse.html')


def radio(request):
    return render(request, 'music/radio.html')
