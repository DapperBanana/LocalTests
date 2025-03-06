
playlist = []

def add_song(song):
    playlist.append(song)
    print(f"{song} has been added to the playlist.")

def remove_song(song):
    if song in playlist:
        playlist.remove(song)
        print(f"{song} has been removed from the playlist.")
    else:
        print(f"{song} is not in the playlist.")

def show_playlist():
    if len(playlist) == 0:
        print("Playlist is empty.")
    else:
        print("Playlist:")
        for idx, song in enumerate(playlist, start=1):
            print(f"{idx}. {song}")

while True:
    print("\nMenu:")
    print("1. Add a song to the playlist")
    print("2. Remove a song from the playlist")
    print("3. Show playlist")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter the song name: ")
        add_song(song)
    elif choice == "2":
        song = input("Enter the song name: ")
        remove_song(song)
    elif choice == "3":
        show_playlist()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
