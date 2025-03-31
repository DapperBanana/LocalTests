
class Playlist:
    def __init__(self):
        self.tracks = []

    def add_track(self, track):
        self.tracks.append(track)
        print(f"{track} has been added to the playlist.")

    def remove_track(self, track):
        if track in self.tracks:
            self.tracks.remove(track)
            print(f"{track} has been removed from the playlist.")
        else:
            print(f"{track} is not in the playlist.")

    def show_playlist(self):
        print("Playlist:")
        for i, track in enumerate(self.tracks):
            print(f"{i+1}. {track}")


playlist = Playlist()

while True:
    print("\n1. Add track to playlist")
    print("2. Remove track from playlist")
    print("3. Show playlist")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        track = input("Enter track name: ")
        playlist.add_track(track)
    elif choice == "2":
        track = input("Enter track name: ")
        playlist.remove_track(track)
    elif choice == "3":
        playlist.show_playlist()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
