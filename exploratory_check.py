
# Movie recommendation system

# List of movies and their genres
movies = {
    "Inception": "Sci-Fi",
    "The Dark Knight": "Action",
    "The Shawshank Redemption": "Drama",
    "Pulp Fiction": "Crime",
    "The Matrix": "Sci-Fi",
    "Fight Club": "Drama",
    "Interstellar": "Sci-Fi",
    "The Godfather": "Crime",
    "The Silence of the Lambs": "Thriller",
    "Goodfellas": "Crime"
}

# Function to recommend movies based on genre
def recommend_movies(genre):
    recommended_movies = []
    for movie in movies:
        if movies[movie] == genre:
            recommended_movies.append(movie)
    
    return recommended_movies

# Main program
print("Welcome to the Movie Recommendation System!")
print("Genres available: Sci-Fi, Action, Drama, Crime, Thriller")
user_input = input("Enter a genre to get movie recommendations: ")

recommended_movies = recommend_movies(user_input)
if recommended_movies:
    print("Recommended movies in the genre", user_input, ":")
    for movie in recommended_movies:
        print("-", movie)
else:
    print("Sorry, no movies found in the selected genre.")
