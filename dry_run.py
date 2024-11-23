
import random

# List of movie genres
genres = ["Action", "Comedy", "Drama", "Horror", "Sci-Fi", "Romance", "Documentary"]

# Dictionary of movie recommendations for each genre
recommendations = {
    "Action": ["The Dark Knight", "Inception", "Mad Max: Fury Road", "Die Hard", "The Avengers"],
    "Comedy": ["Superbad", "The Hangover", "Anchorman", "Bridesmaids", "Step Brothers"],
    "Drama": ["The Shawshank Redemption", "Forrest Gump", "Titanic", "The Godfather", "Schindler's List"],
    "Horror": ["The Exorcist", "Get Out", "A Nightmare on Elm Street", "The Shining", "Halloween"],
    "Sci-Fi": ["Blade Runner", "Interstellar", "The Matrix", "E.T. the Extra-Terrestrial", "Alien"],
    "Romance": ["The Notebook", "Titanic", "Pride and Prejudice", "La La Land", "The Fault in Our Stars"],
    "Documentary": ["13th", "Blackfish", "Won't You Be My Neighbor?", "Fahrenheit 9/11", "March of the Penguins"]
}

# Function to recommend a movie based on user's genre choice
def recommend_movie(genre):
    if genre in genres:
        movie = random.choice(recommendations[genre])
        print(f"We recommend watching '{movie}' in the {genre} genre!")
    else:
        print("Invalid genre choice. Please choose a valid genre.")

# Main function
def main():
    print("Welcome to the Movie Recommendation System!")
    print("Here are the available genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{idx}. {genre}")
    
    genre_choice = int(input("Choose a genre (enter the corresponding number): "))
    
    if 1 <= genre_choice <= len(genres):
        recommend_movie(genres[genre_choice - 1])
    else:
        print("Invalid genre choice. Please try again.")
    
if __name__ == "__main__":
    main()
