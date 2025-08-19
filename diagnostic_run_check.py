
playlist = []

def add_song():
    song = input("Enter the name of the song: ")
    artist = input("Enter the name of the artist: ")
    playlist.append({"song": song, "artist": artist})
    print(f"{song} by {artist} has been added to the playlist")

def remove_song():
    song = input("Enter the name of the song you want to remove: ")
    artist = input("Enter the name of the artist: ")
    for idx, track in enumerate(playlist):
        if track["song"] == song and track["artist"] == artist:
            playlist.pop(idx)
            print(f"{song} by {artist} has been removed from the playlist")
            return
    print("Song not found in the playlist")

def display_playlist():
    if not playlist:
        print("Playlist is empty")
    else:
        print("Current playlist:")
        for idx, track in enumerate(playlist):
            print(f"{idx+1}. {track['song']} by {track['artist']}")

def main():
    while True:
        print("\nMenu:")
        print("1. Add song")
        print("2. Remove song")
        print("3. Display playlist")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_song()
        elif choice == "2":
            remove_song()
        elif choice == "3":
            display_playlist()
        elif choice == "4":
            print("Exiting program")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
