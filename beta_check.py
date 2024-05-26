
class PlaylistManager:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"{song} has been added to the playlist.")
    
    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"{song} has been removed from the playlist.")
        else:
            print(f"{song} is not in the playlist.")
    
    def show_playlist(self):
        if self.playlist:
            print("Playlist:")
            for i, song in enumerate(self.playlist, 1):
                print(f"{i}. {song}")
        else:
            print("Playlist is empty.")
    
    def clear_playlist(self):
        self.playlist = []
        print("Playlist has been cleared.")

    def play_playlist(self):
        if self.playlist:
            print("Playing playlist:")
            for song in self.playlist:
                print(f"Now playing: {song}")
        else:
            print("Playlist is empty. Add some songs to play.")

# Main program
playlist_manager = PlaylistManager()

while True:
    print("\n1. Add a song to the playlist")
    print("2. Remove a song from the playlist")
    print("3. Show playlist")
    print("4. Clear playlist")
    print("5. Play playlist")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        song = input("Enter the name of the song: ")
        playlist_manager.add_song(song)
    elif choice == "2":
        song = input("Enter the name of the song to remove: ")
        playlist_manager.remove_song(song)
    elif choice == "3":
        playlist_manager.show_playlist()
    elif choice == "4":
        playlist_manager.clear_playlist()
    elif choice == "5":
        playlist_manager.play_playlist()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
