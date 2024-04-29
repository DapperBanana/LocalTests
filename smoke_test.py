
class PlaylistManager:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"{song} added to playlist.")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"{song} removed from playlist.")
        else:
            print(f"{song} not found in playlist.")

    def show_playlist(self):
        if self.playlist:
            print("Current Playlist:")
            for index, song in enumerate(self.playlist):
                print(f"{index+1}. {song}")
        else:
            print("Playlist is empty.")

def main():
    playlist_manager = PlaylistManager()

    while True:
        print("\n1. Add song to playlist")
        print("2. Remove song from playlist")
        print("3. Show playlist")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            song = input("Enter song name: ")
            playlist_manager.add_song(song)
        elif choice == '2':
            song = input("Enter song name: ")
            playlist_manager.remove_song(song)
        elif choice == '3':
            playlist_manager.show_playlist()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
