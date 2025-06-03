
playlist = []

def display_menu():
    print("Music Playlist Manager")
    print("1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. Show playlist")
    print("4. Exit")

def add_song():
    song = input("Enter song name: ")
    playlist.append(song)
    print("Song added to playlist!")

def remove_song():
    song = input("Enter song name to remove: ")
    if song in playlist:
        playlist.remove(song)
        print("Song removed from playlist!")
    else:
        print("Song not found in playlist.")

def show_playlist():
    if len(playlist) == 0:
        print("Playlist is empty")
    else:
        print("Playlist:")
        for index, song in enumerate(playlist, start=1):
            print(f"{index}. {song}")

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_song()
    elif choice == '2':
        remove_song()
    elif choice == '3':
        show_playlist()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")
