
import random

# Define a dictionary mapping genres to lists of movie titles
movies = {
    "action": ["The Dark Knight", "Inception", "Mad Max: Fury Road"],
    "comedy": ["Superbad", "Bridesmaids", "The Hangover"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
    "romance": ["The Notebook", "La La Land", "Pride and Prejudice"]
}

def recommend_movie():
    # Prompt the user to enter a genre
    genre = input("Enter a movie genre (action, comedy, drama, romance): ").lower()
    
    # Check if the genre is in the dictionary
    if genre in movies:
        # Select a random movie title from the list of movies in that genre
        movie = random.choice(movies[genre])
        print(f"We recommend you watch: {movie}")
    else:
        print("Genre not found. Please try again.")

# Main program loop
while True:
    recommend_movie()
    response = input("Would you like another recommendation? (yes/no) ").lower()
    if response != "yes":
        break
