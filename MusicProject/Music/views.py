from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'music/home.html')


def index(request):
    # return HttpResponse('This is the landing page')
    return render(request, 'music/index.html')


def browse(request):
    return render(request, 'music/browse.html')


def radio(request):
    return render(request, 'music/radio.html')
