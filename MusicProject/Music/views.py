from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('This is the music home page!')
    return render(request, 'home.html')


def index(request):
    # return HttpResponse('This is the landing page')
    return render(request, 'index.html')
