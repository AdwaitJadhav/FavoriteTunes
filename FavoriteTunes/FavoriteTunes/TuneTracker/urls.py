from django.urls import path
from . import views

urlpatterns = [
    path('', views.TuneTracker, name='TuneTracker'),
    path('<int:song_id>/', views.song_details, name='song_detail'),
    path('add_song/', views.add_song_view, name='add_song'),
    path('delete_song/<int:song_id>/', views.delete_song_view, name='delete_song'),
]