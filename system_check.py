
class PlaylistManager:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"Added {song} to the playlist.")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"Removed {song} from the playlist.")
        else:
            print(f"{song} is not in the playlist.")

    def show_playlist(self):
        print("Current Playlist:")
        for i, song in enumerate(self.playlist):
            print(f"{i+1}. {song}")

    def clear_playlist(self):
        self.playlist = []
        print("Playlist cleared.")

    def play_next_song(self):
        if self.playlist:
            next_song = self.playlist.pop(0)
            print(f"Now playing: {next_song}")
        else:
            print("Playlist is empty.")

playlist_manager = PlaylistManager()

while True:
    print("\n1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Show playlist")
    print("4. Clear playlist")
    print("5. Play next song")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        song = input("Enter the song name: ")
        playlist_manager.add_song(song)
    elif choice == '2':
        song = input("Enter the song name: ")
        playlist_manager.remove_song(song)
    elif choice == '3':
        playlist_manager.show_playlist()
    elif choice == '4':
        playlist_manager.clear_playlist()
    elif choice == '5':
        playlist_manager.play_next_song()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
