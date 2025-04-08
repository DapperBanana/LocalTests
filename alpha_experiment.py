
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
        print("Current Playlist:")
        for i, song in enumerate(self.playlist, 1):
            print(f"{i}. {song}")

playlist_manager = PlaylistManager()

while True:
    print("\n1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Show playlist")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        song = input("Enter the name of the song: ")
        playlist_manager.add_song(song)
    elif choice == '2':
        song = input("Enter the name of the song you want to remove: ")
        playlist_manager.remove_song(song)
    elif choice == '3':
        playlist_manager.show_playlist()
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
