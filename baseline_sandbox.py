
# Import necessary libraries
import random

# Create a list of movies
movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Goodfellas", 
          "Schindler's List", "Inception", "The Lord of the Rings: The Return of the King", "Fight Club", 
          "The Matrix", "Forrest Gump", "The Silence of the Lambs", "The Avengers", "Interstellar", 
          "Gladiator", "The Departed", "The Prestige", "Casablanca", "Eternal Sunshine of the Spotless Mind", 
          "Titanic"]

# Create a function to recommend a movie
def recommend_movie():
    recommended_movie = random.choice(movies)
    return recommended_movie

# Create a function to display the recommended movie
def display_movie(recommended_movie):
    print("Recommended Movie: {}".format(recommended_movie))

# Main code to run the program
print("Welcome to the Movie Recommendation System!")
while True:
    user_input = input("\nWould you like a movie recommendation? (Y/N): ")
    
    if user_input.upper() == "Y":
        recommended_movie = recommend_movie()
        display_movie(recommended_movie)
    elif user_input.upper() == "N":
        print("Thank you for using the Movie Recommendation System. Have a great day!")
        break
    else:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
