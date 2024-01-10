from django.db import models
#artist model
class Artist(models.Model):
    name = models.CharField(max_length=255, unique=True)

#song model
class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    

