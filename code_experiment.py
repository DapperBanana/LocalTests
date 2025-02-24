
import random

# List of movies
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Schindler's List", "The Lord of the Rings: The Return of the King", "Forrest Gump", "Inception", "The Matrix", "The Silence of the Lambs"]

# Function to recommend a movie
def recommend_movie():
    print("Welcome to the movie recommendation system!")
    input("Press Enter to get a movie recommendation.")
    recommended_movie = random.choice(movies)
    print("I recommend you watch:", recommended_movie)

# Main program
while True:
    recommend_movie()
    repeat = input("Would you like another recommendation? (yes/no): ")
    if repeat.lower() != 'yes':
        break
