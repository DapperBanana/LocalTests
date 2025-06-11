
playlist = []

def add_song():
    song = input("Enter the name of the song: ")
    artist = input("Enter the artist of the song: ")
    playlist.append({"song": song, "artist": artist})
    print("Song added to playlist.")

def remove_song():
    song = input("Enter the name of the song you want to remove: ")
    for item in playlist:
        if item["song"] == song:
            playlist.remove(item)
            print("Song removed from playlist.")
            return
    print("Song not found in playlist.")

def display_playlist():
    if len(playlist) == 0:
        print("Playlist is empty.")
    else:
        for i, item in enumerate(playlist, 1):
            print(f"{i}. {item['song']} by {item['artist']}")

while True:
    print("\nSelect an option:")
    print("1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Display playlist")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_song()
    elif choice == '2':
        remove_song()
    elif choice == '3':
        display_playlist()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
