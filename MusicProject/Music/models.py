from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

# class Images(models.Model):

#     img_id = models.CharField(max_length=10, primary_key=True)
#     p = os.path.dirname(os.path.dirname(__file__))
#     p = os.path.join(p, 'media/images')
#     path = models.FileField(upload_to="images/", null=True)
#     img_name = models.CharField(max_length=20)


class Genre(models.Model):
    #    genre_id = models.CharField(max_length=10, primary_key=True)
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class Album(models.Model):
    #image = models.OneToOneField(Images, on_delete=models.CASCADE)
    #genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    #song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    image = models.FileField(upload_to="images/songs", null=True)
    genre = models.ManyToManyField(Genre)
    album_name = models.CharField(max_length=100)
    total_tracks = models.IntegerField()

    def __str__(self):
        return self.album_name


class Song(models.Model):
    #song_id = models.CharField(max_length=10, primary_key=True)
    #image = models.OneToOneField(Images, on_delete=models.CASCADE)
    songName = models.CharField(max_length=50, null=True)
    song_path = models.FileField(upload_to="songs/", null=True)
    image = models.FileField(upload_to="images/song", null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.songName


class Singer(models.Model):
    #singer_id = models.CharField(max_length=10, primary_key=True)
    #image = models.OneToOneField(Images, on_delete=models.CASCADE)
    singer_name = models.CharField(max_length=50)
    total_songs = models.IntegerField()
    total_albums = models.IntegerField()
    songs = models.ManyToManyField(Song)
    image = models.FileField(upload_to="images/singer", null=True)
    album=models.ManyToManyField(Album)
    def __str__(self):
        return self.singer_name


class Playlist(models.Model):
    #playlist_id = models.CharField(max_length=10, primary_key=True)
    playlist_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.playlist_name


class Artist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)

    def __str__(self):
        return "User %s: Artist %s" % (self.user.username, self.singer.singer_name)


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
