
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)
    
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print("Song not found in playlist.")
    
    def display_playlist(self):
        print(f"Playlist: {self.name}")
        for index, song in enumerate(self.songs, start=1):
            print(f"{index}. {song}")
    
# Create a playlist
my_playlist = Playlist("My Playlist")

# Add songs to the playlist
my_playlist.add_song("Song 1")
my_playlist.add_song("Song 2")
my_playlist.add_song("Song 3")

# Display the playlist
my_playlist.display_playlist()

# Remove a song
my_playlist.remove_song("Song 2")

# Display the updated playlist
my_playlist.display_playlist()
