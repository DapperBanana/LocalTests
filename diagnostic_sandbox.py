
# Movie recommendation system

# Sample movie data
movies = {
    'The Shawshank Redemption': ['Drama'],
    'The Godfather': ['Drama', 'Crime'],
    'The Dark Knight': ['Action', 'Crime', 'Drama'],
    'Pulp Fiction': ['Crime', 'Drama'],
    'Forrest Gump': ['Drama', 'Romance'],
    'Fight Club': ['Drama'],
    'Inception': ['Action', 'Adventure', 'Sci-Fi'],
    'Interstellar': ['Adventure', 'Drama', 'Sci-Fi']
}

# Function to recommend movies based on user input
def recommend_movies(genres):
    recommended_movies = []
    for movie, movie_genres in movies.items():
        if any(genre in movie_genres for genre in genres):
            recommended_movies.append(movie)
    return recommended_movies

# Main program
print("Welcome to the Movie Recommendation System!")
print("Available genres: Drama, Crime, Action, Romance, Adventure, Sci-Fi")

input_genres = input("Enter your preferred genres (comma separated): ").split(',')
recommended_movies = recommend_movies(input_genres)

if recommended_movies:
    print("Recommended movies:")
    for movie in recommended_movies:
        print(movie)
else:
    print("No movies matching the genres provided.")
