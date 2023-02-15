"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlist_songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement= True) 
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'), primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id'), primary_key=True)

class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement= True) 
    title = db.Column(db.String(150), nullable=False) 
    artist = db.Column(db.String(150), nullable = False) 

    playlist = db.relationship('PlaylistSong', backref='songs')


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable = False) 
    description = db.Column(db.Text) 

    songs = db.relationship('PlaylistSong', backref='playlist')
    
    







# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
