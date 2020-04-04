from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Images(models.Model):
    img_id=models.CharField(max_length=10,primary_key=True)
    path=models.FilePathField(max_length=100)
    img_name=models.CharField(max_length=20)

class Song(models.Model):
    singer_id=models.CharField(max_length=10,primary_key=True)
    img_id = models.OneToOneField(Images, on_delete=models.CASCADE)
    song_path=models.FilePathField(max_length=100)

class Singer(models.Model):
    singer_id=models.CharField(max_length=10,primary_key=True)
    singer_name=models.CharField(max_length=50)
    img_id = models.OneToOneField(Images, on_delete=models.CASCADE)
    total_songs=models.IntegerField()
    total_albums=models.IntegerField()
    songs=models.ManyToManyField(Song)
    

class Playlists(models.Model):
    playlist_id=models.CharField(max_length=10,primary_key=True)
    playlist_name=models.CharField(max_length=10)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    songs=models.ManyToManyField(Song)

class Artist(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    singer_id=models.ForeignKey(Singer, on_delete=models.CASCADE)

class Favorites(models.Model):
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    song_id=models.ForeignKey(Song, on_delete=models.CASCADE)

class Genre(models.Model):
    genre_id= models.CharField(max_length=10,primary_key=True)
    genre_name = models.CharField(max_length=100)

class Album(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    img_id = models.OneToOneField(Images, on_delete=models.CASCADE)
    genre_id= models.ForeignKey(Genre, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    album_id=models.CharField(max_length=10,primary_key=True)
    total_tracks=models.IntegerField()


