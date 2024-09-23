
# Sample dataset of movies and their genres
movies = {
    "The Shawshank Redemption": ["Drama"],
    "The Godfather": ["Crime", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "The Avengers": ["Action", "Adventure"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "The Lion King": ["Animation", "Adventure", "Drama"]
}

# Function to recommend movies based on user's preferences
def recommend_movies(user_preference):
    recommended_movies = []
    
    for movie in movies:
        if any(genre in user_preference for genre in movies[movie]):
            recommended_movies.append(movie)
    
    return recommended_movies

# Sample user preferences
user_preferences = ["Drama", "Adventure"]

# Get recommended movies based on user's preferences
recommended_movies = recommend_movies(user_preferences)
print("Recommended movies based on your preferences:")
for movie in recommended_movies:
    print(movie)
