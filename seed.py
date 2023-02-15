from models import db, Playlist, Song, PlaylistSong
from app import app 

db.drop_all() 
db.create_all()

playlist_1 = Playlist(
    name='Swim Deep', 
    description='A sad playlist' 
)

playlist_2 = Playlist(
    name='time machine', 
    description='a old playlist with rock n roll' 
)

song_1 = Song(
    title='Welcome to the jungle',
    artist='Guns n roses' 
)

song_2 = Song(
    title='Love in the rain', 
    artist='rihanna' 
)

song_3 = Song(
    title='Hotline Bling', 
    artist='Drake'
)

swim_deep = PlaylistSong(
    playlist_id=1, 
    song_id = 2
)
swim_deep2 = PlaylistSong(
    playlist_id=1, 
    song_id = 3
)
time_machine = PlaylistSong(
    playlist_id=2, 
    song_id = 1
)
time_machine2 = PlaylistSong(
    playlist_id=1, 
    song_id = 3
)

db.session.add_all([playlist_1, playlist_2, song_1, song_2, song_3, swim_deep, swim_deep2, time_machine, time_machine2])
db.session.commit()