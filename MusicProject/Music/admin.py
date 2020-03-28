from django.contrib import admin
from .models import Singer, Album, Song

# Register your models here.
admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Song)
