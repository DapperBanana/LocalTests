
# Basic text-based movie recommendation system

# Movie database
movies = {
    "The Shawshank Redemption": ["Drama", "Crime"],
    "The Godfather": ["Drama", "Crime"],
    "The Dark Knight": ["Action", "Crime"],
    "Pulp Fiction": ["Drama", "Crime"],
    "Forrest Gump": ["Drama", "Romance"],
    "Inception": ["Action", "Sci-Fi"],
    "The Matrix": ["Action", "Sci-Fi"],
}

# Function to recommend movies based on genre
def recommend_movies(genre):
    recommended_movies = []
    for movie, genres in movies.items():
        if genre in genres:
            recommended_movies.append(movie)
    
    return recommended_movies

# Main program
print("Welcome to the Movie Recommendation System!")
print("Choose a genre to get movie recommendations.")
print("Genres available: Drama, Crime, Action, Romance, Sci-Fi")
selected_genre = input("Enter a genre: ")

recommended_movies = recommend_movies(selected_genre)
if recommended_movies:
    print("Movies recommended for", selected_genre, "genre:")
    for movie in recommended_movies:
        print("-", movie)
else:
    print("No movies found for", selected_genre, "genre. Please try another genre.")
