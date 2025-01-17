
class MusicPlaylist:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"{song} added to playlist")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"{song} removed from playlist")
        else:
            print(f"{song} not found in playlist")

    def show_playlist(self):
        if not self.playlist:
            print("No songs in playlist")
        else:
            print("Playlist:")
            for idx, song in enumerate(self.playlist, start=1):
                print(f"{idx}. {song}")

def main():
    playlist = MusicPlaylist()

    while True:
        print("\n1. Add song to playlist")
        print("2. Remove song from playlist")
        print("3. Show playlist")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            song = input("Enter song name: ")
            playlist.add_song(song)
        elif choice == "2":
            song = input("Enter song name: ")
            playlist.remove_song(song)
        elif choice == "3":
            playlist.show_playlist()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
