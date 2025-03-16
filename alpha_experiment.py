
def show_menu():
    print("\n---- Music Playlist Manager ----")
    print("1. Add song to playlist")
    print("2. Remove song from playlist")
    print("3. View playlist")
    print("4. Exit")

def add_song(playlist):
    song = input("\nEnter the name of the song: ")
    playlist.append(song)
    print(f"Added {song} to playlist")

def remove_song(playlist):
    song = input("\nEnter the name of the song to remove: ")
    if song in playlist:
        playlist.remove(song)
        print(f"Removed {song} from playlist")
    else:
        print(f"{song} not found in playlist")

def view_playlist(playlist):
    print("\n--- Playlist ---")
    for i, song in enumerate(playlist, 1):
        print(f"{i}. {song}")

def main():
    playlist = []
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_song(playlist)
        elif choice == '2':
            remove_song(playlist)
        elif choice == '3':
            view_playlist(playlist)
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
