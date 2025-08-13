
class MusicPlaylist:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)
        print(f"{song} added to the playlist.")

    def remove_song(self, song):
        if song in self.playlist:
            self.playlist.remove(song)
            print(f"{song} removed from the playlist.")
        else:
            print(f"{song} is not in the playlist.")

    def show_playlist(self):
        if self.playlist:
            print("Playlist:")
            for idx, song in enumerate(self.playlist, start=1):
                print(f"{idx}. {song}")
        else:
            print("Playlist is empty.")


def main():
    playlist = MusicPlaylist()

    while True:
        print("\nMenu:")
        print("1. Add song to playlist")
        print("2. Remove song from playlist")
        print("3. Show playlist")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            song = input("Enter the name of the song: ")
            playlist.add_song(song)
        elif choice == "2":
            song = input("Enter the name of the song: ")
            playlist.remove_song(song)
        elif choice == "3":
            playlist.show_playlist()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
