
playlist = []

def add_song(song):
    playlist.append(song)

def remove_song(song):
    if song in playlist:
        playlist.remove(song)
    else:
        print("Song not found in playlist.")

def display_playlist():
    if not playlist:
        print("Playlist is empty.")
    else:
        print("Current playlist:")
        for i, song in enumerate(playlist):
            print(f"{i+1}. {song}")

while True:
    print("\nMenu:")
    print("1. Add a song to playlist")
    print("2. Remove a song from playlist")
    print("3. Display playlist")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        song = input("Enter the name of the song: ")
        add_song(song)
        print(f"Added '{song}' to playlist.")
    
    elif choice == '2':
        song = input("Enter the name of the song to remove: ")
        remove_song(song)
    
    elif choice == '3':
        display_playlist()
    
    elif choice == '4':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
