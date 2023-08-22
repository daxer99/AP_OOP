import pandas as pd
def read_file(filename):
    data = pd.read_csv(filename,sep=",")
    return data.values.tolist()

class Song:
    def __init__(self,title,artist,genre,year,dur):
        self.title = title
        self.artist= artist
        self.genre = genre
        self.year = year
        self.dur = dur
    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def get_genre(self):
        return self.genre
    def get_year(self):
        return self.year
    def get_dur(self):
        return round(int(self.dur)/60,2)

class Playlist:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        self.songs = []

    def add_song(self,song):
        self.songs.append(song)

    def get_duration(self):
        dur = 0
        for i in range(len(self.songs)):
            dur +=self.songs[i].get_dur()
        return round(dur,2)

filename = "/media/rodrigo/Datos/Facultad/FIUNER/Fundamentos/AP_OOP/Evaluacion/Spotify 2010 - 2019 Top 100.csv"
data = read_file(filename)

data_songs = []
for i in range(len(data)):
    data_songs.append(Song(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
    print(data_songs[i].get_year())

pl_2011 = Playlist("2011","Rodrigo")
for i in range(len(data_songs)):
    if int(data_songs[i].get_year()) == 2011:
        pl_2011.add_song(data_songs[i])
print(pl_2011.get_duration())

pl_indie = Playlist("Indie","Rodrigo")
for i in range(len(data_songs)):
    if data_songs[i].get_genre() == "indie rock":
        pl_indie.add_song(data_songs[i])
print(pl_indie.get_duration())