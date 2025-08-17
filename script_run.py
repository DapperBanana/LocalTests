
# Sample data of movies and their genres
movies_data = {
    "Movie1": ["Action", "Comedy"],
    "Movie2": ["Drama", "Romance"],
    "Movie3": ["Action", "Thriller"],
    "Movie4": ["Comedy", "Romance"],
    "Movie5": ["Drama", "Thriller"]
}

# Function to recommend movies based on user's preferences
def recommend_movies(user_preferences):
    recommended_movies = []
    
    for movie, genres in movies_data.items():
        intersection = set(genres) & set(user_preferences)
        if intersection:
            recommended_movies.append(movie)
    
    return recommended_movies

# Testing the recommendation system
user_preferences = ["Action", "Thriller"]
recommended_movies = recommend_movies(user_preferences)

print("Recommended movies based on your preferences:")
for movie in recommended_movies:
    print(movie)
