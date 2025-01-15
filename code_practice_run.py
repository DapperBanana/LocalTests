
class PlaylistManager:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"Added '{song}' to the playlist.")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"Removed '{song}' from the playlist.")
        else:
            print(f"'{song}' is not in the playlist.")

    def show_playlist(self):
        if self.playlist:
            print("Current Playlist:")
            for idx, song in enumerate(self.playlist, start=1):
                print(f"{idx}. {song}")
        else:
            print("Playlist is empty.")

    def clear_playlist(self):
        self.playlist = []
        print("Playlist cleared.")

playlist_manager = PlaylistManager()

while True:
    print("\nMenu:")
    print("1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Show playlist")
    print("4. Clear playlist")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter song name: ")
        playlist_manager.add_song(song)
    elif choice == "2":
        song = input("Enter song name: ")
        playlist_manager.remove_song(song)
    elif choice == "3":
        playlist_manager.show_playlist()
    elif choice == "4":
        playlist_manager.clear_playlist()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
