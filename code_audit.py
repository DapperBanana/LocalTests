letion(id='chatcmpl-9e5gNE2IWa3tzsFgttQV2Lfu1ofdP', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='import random

# Initialize an empty playlist
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

def display_playlist():
    print("Current Playlist:")
    for song in playlist:
        print(song)

# Main program loop
while True:
    print("\nChoose an option:")
    print("1. Add a song to the playlist")
    print("2. Remove a song from the playlist")
    print("3. Display the playlist")
    print("4. Shuffle the playlist")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        song = input("Enter the name of the song: ")
        add_song(song)
    
    elif choice == "2":
        song = input("Enter the name of the song: ")
        remove_song(song)
    
    elif choice == "3":
        display_playlist()
    
    elif choice == "4":
        random.shuffle(playlist)
        print("Playlist shuffled.")
    
    elif choice == "5":
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please try again.")', role='assistant', function_call=None, tool_calls=None))], created=1719341991, model='gpt-3.5-turbo-0125', object='chat.completion', system_fingerprint=None, usage=CompletionUsage(completion_tokens=287, prompt_tokens=21, total_tokens=308)