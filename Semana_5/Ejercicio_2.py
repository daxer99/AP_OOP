class User:
    def __init__(self, username, password, email, premium=False):
        self.username = username
        self.password = password
        self.email = email
        self.premium = premium
        self.playlists = []

    def create_playlist(self, name, public):
        playlist = Playlist(name, public)
        self.playlists.append(playlist)
        return playlist

    def add_song_to_playlist(self, playlist, song):
        playlist.add_song(song)


class Song:
    def __init__(self, title, artist, album, genre, length):
        self.title = title
        self.artist = artist
        self.album = album
        self.genre = genre
        self.length = length


class Playlist:
    def __init__(self, name, public):
        self.name = name
        self.public = public
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


class Library:
    def __init__(self):
        self.users = []

    def create_user(self, username, password, email):
        user = User(username, password, email)
        self.users.append(user)
        return user

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def create_playlist(self, user, name, public):
        return user.create_playlist(name, public)

    def add_song_to_playlist(self, user, playlist, song):
        if playlist in user.playlists:
            user.add_song_to_playlist(playlist, song)

class MusicService:
    def __init__(self, library):
        self.library = library

    def search_songs(self, query):
        songs = []
        for user in self.library.users:
            for playlist in user.playlists:
                for song in playlist.s:
                    if song == query:
                        return song
                    else:
                        return None