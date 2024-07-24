
playlist = []

def display_menu():
    print("\n1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. View playlist")
    print("4. Exit")

def add_song():
    song = input("Enter song name: ")
    playlist.append(song)
    print(f"{song} added to playlist")

def remove_song():
    if len(playlist) == 0:
        print("Playlist is empty.")
    else:
        print("Current Playlist:")
        for index, song in enumerate(playlist):
            print(f"{index + 1}. {song}")
        
        song_index = int(input("Enter song number to remove: ")) - 1
        if song_index < 0 or song_index >= len(playlist):
            print("Invalid song number.")
        else:
            removed_song = playlist.pop(song_index)
            print(f"{removed_song} removed from playlist.")

def view_playlist():
    if len(playlist) == 0:
        print("Playlist is empty.")
    else:
        print("Current Playlist:")
        for index, song in enumerate(playlist):
            print(f"{index + 1}. {song}")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_song()
    elif choice == '2':
        remove_song()
    elif choice == '3':
        view_playlist()
    elif choice == '4':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
