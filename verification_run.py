
def display_menu():
    print("-------------------------------")
    print("1. Add a song to the playlist")
    print("2. Remove a song from the playlist")
    print("3. Show all songs in the playlist")
    print("4. Exit")
    print("-------------------------------")

playlist = []

while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        song = input("Enter the song name: ")
        playlist.append(song)
        print("Song added to the playlist.")

    elif choice == '2':
        song = input("Enter the song name to remove: ")
        if song in playlist:
            playlist.remove(song)
            print("Song removed from the playlist.")
        else:
            print("Song not found in the playlist.")

    elif choice == '3':
        if len(playlist) == 0:
            print("Playlist is empty.")
        else:
            print("Songs in the playlist:")
            for i, song in enumerate(playlist, start=1):
                print(f"{i}. {song}")

    elif choice == '4':
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
