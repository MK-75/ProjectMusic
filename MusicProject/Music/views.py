from django.shortcuts import render
from django.http import HttpResponse
from Music.models import *

# Create your views here.


def home(request):
    song = Song.objects.get(pk=4)
    context = {'song': song}
    return render(request, 'music/home.html', context)


# def index(request):
#     # return HttpResponse('This is the landing page')
#     return render(request, 'index.html')


def browse(request):
    return render(request, 'music/browse.html')


def radio(request):
    return render(request, 'music/radio.html')
