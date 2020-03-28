from django.db import models

# Create your models here.


class Singer(models.Model):
    singer_name = models.CharField(max_length=100)


class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
