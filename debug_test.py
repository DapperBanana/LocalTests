
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, title, artist):
        self.songs.append({
            'title': title,
            'artist': artist
        })
        print(f'\n{title} by {artist} added to playlist.')

    def display_playlist(self):
        if len(self.songs) == 0:
            print("\nPlaylist is empty.")
        else:
            print("\n Playlist:")
            for i, song in enumerate(self.songs):
                print(f"{i+1}. {song['title']} by {song['artist']}")

    def remove_song(self, index):
        if index < 1 or index > len(self.songs):
            print("\nInvalid index.")
        else:
            removed_song = self.songs.pop(index-1)
            print(f"\n{removed_song['title']} by {removed_song['artist']} removed from playlist.")


def main():
    playlist = Playlist()

    while True:
        print("\nMusic Playlist Manager")
        print("1. Add Song")
        print("2. Display Playlist")
        print("3. Remove Song")
        print("4. Exit")

        choice = input("\nEnter choice: ")

        if choice == '1':
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            playlist.add_song(title, artist)
        elif choice == '2':
            playlist.display_playlist()
        elif choice == '3':
            index = int(input("Enter index of song to remove: "))
            playlist.remove_song(index)
        elif choice == '4':
            print("\nThank you for using the Playlist Manager.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
