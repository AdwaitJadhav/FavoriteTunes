from django.shortcuts import render, redirect
from .models import Song, Artist


def TuneTracker(request): #main page view
    songs = Song.objects.all()
    artists = Artist.objects.all()
    artist_song_counts = {artist.name: artist.songs.count() for artist in artists}
    #sorting the artist_song_count dictionary to display top artists
    sorted_artist_song_counts = dict( 
        sorted(artist_song_counts.items(), key=lambda item: item[1], reverse=True)
    )
    return render(request, 'index.html', {'songs_list': songs, 'artist_list':artists, 'artist_counts':sorted_artist_song_counts})

def song_details(request, song_id): #song details view to display title and artist of song
    song = Song.objects.get(pk=song_id)
    return render(request, 'song_details.html', {'song': song})

def add_song_view(request): #view to add song from web page, redirects back to the main page
    if request.method == 'POST':
        song_title = request.POST.get('song_title')
        artist_id = request.POST.get('artist_name')
        new_artist_name = request.POST.get('new_artist')

        if artist_id == 'new' and new_artist_name:
            new_artist = Artist.objects.create(name=new_artist_name)
            artist_id = new_artist.id

        new_song = Song.objects.create(title=song_title, artist_id=artist_id)
        return redirect('TuneTracker')

    artists = Artist.objects.all()
    return render(request, 'index.html', {'artist_list': artists})

def delete_song_view(request, song_id):# view to delete song from list, redirects back to main page
    song = Song.objects.get(pk=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('TuneTracker')
    return redirect('TuneTracker')
