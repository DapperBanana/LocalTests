
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print("Song not found in the playlist.")

    def show_playlist(self):
        if len(self.songs) == 0:
            print("Playlist is empty.")
        else:
            for i, song in enumerate(self.songs):
                print(f"{i+1}. {song}")

playlist = Playlist()

while True:
    print("\nMusic Playlist Manager")
    print("1. Add a song")
    print("2. Remove a song")
    print("3. Show playlist")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        song = input("Enter the name of the song: ")
        playlist.add_song(song)
    elif choice == "2":
        song = input("Enter the name of the song you want to remove: ")
        playlist.remove_song(song)
    elif choice == "3":
        playlist.show_playlist()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
