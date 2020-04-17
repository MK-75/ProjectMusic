from django.urls import path
from Music import views


app_name = 'music'

urlpatterns = [
    path('ArtistSelect/', views.artistSelect, name='artistSelect'),
    path('<str:name>/', views.specificAlbum, name='specificAlbum'),
    path('browse/', views.browse, name='browse'),
    path('radio/', views.radio, name='radio'),
    path('', views.home, name='home')
]
