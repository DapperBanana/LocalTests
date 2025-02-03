
# Movie recommendation system

# List of movies and their genres
movies = {
    "The Shawshank Redemption": "Drama",
    "The Godfather": "Crime",
    "The Dark Knight": "Action",
    "Forrest Gump": "Drama",
    "Pulp Fiction": "Crime",
    "The Matrix": "Action",
    "Titanic": "Romance"
}

# Get user input for genre preference
user_input = input("Enter your preferred genre (Drama, Crime, Action, Romance): ")

# Find and recommend movies based on user input
recommended_movies = []
for movie, genre in movies.items():
    if genre == user_input:
        recommended_movies.append(movie)

# Display recommended movies
if recommended_movies:
    print("Recommended movies for you:")
    for movie in recommended_movies:
        print(movie)
else:
    print("No movies found in the specified genre.")
