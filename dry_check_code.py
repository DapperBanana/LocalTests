
playlist = []

while True:
    print("1. Add a song to the playlist")
    print("2. View the playlist")
    print("3. Remove a song from the playlist")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        song_name = input("Enter the name of the song: ")
        artist_name = input("Enter the name of the artist: ")
        playlist.append((song_name, artist_name))
        print("Song added to the playlist.")
    elif choice == 2:
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            print("Playlist:")
            for i, (song, artist) in enumerate(playlist, 1):
                print(f"{i}. {song} by {artist}")
    elif choice == 3:
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            index = int(input("Enter the index of the song to remove: ")) - 1
            if index < 0 or index >= len(playlist):
                print("Invalid index.")
            else:
                removed_song = playlist.pop(index)
                print(f"{removed_song[0]} by {removed_song[1]} removed from the playlist.")
    elif choice == 4:
        print("Exiting playlist manager.")
        break
    else:
        print("Invalid choice. Please try again.")
