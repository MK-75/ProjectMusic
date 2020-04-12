from django.urls import path
from Music import views


app_name = 'music'

urlpatterns = [
    #path('<album_name>/', views.specificAlbum, name='album'),
    path('browse/', views.browse, name='browse'),
    path('radio/', views.radio, name='radio'),
    path('', views.home, name='home')
]
