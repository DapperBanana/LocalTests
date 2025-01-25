
playlist = []

def add_song():
    song = input("Enter the name of the song: ")
    artist = input("Enter the name of the artist: ")
    playlist.append({"song": song, "artist": artist})
    print(f"{song} by {artist} has been added to the playlist.")

def remove_song():
    if playlist:
        print("Current Playlist:")
        for i, song in enumerate(playlist):
            print(f"{i+1}. {song['song']} by {song['artist']}")
        index = int(input("Enter the number of the song you want to remove: ")) - 1
        if index in range(len(playlist)):
            removed_song = playlist.pop(index)
            print(f"{removed_song['song']} by {removed_song['artist']} has been removed from the playlist.")
        else:
            print("Invalid song number.")
    else:
        print("Playlist is empty.")

def view_playlist():
    if playlist:
        print("Current Playlist:")
        for i, song in enumerate(playlist):
            print(f"{i+1}. {song['song']} by {song['artist']}")
    else:
        print("Playlist is empty.")

def main():
    while True:
        print("\nMENU:")
        print("1. Add a song to the playlist")
        print("2. Remove a song from the playlist")
        print("3. View playlist")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_song()
        elif choice == "2":
            remove_song()
        elif choice == "3":
            view_playlist()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
