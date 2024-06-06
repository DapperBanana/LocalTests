
# Sample content-based recommendation system

# Sample user profiles and their preferences
user_profiles = {
    'Alice': {'action': 5, 'comedy': 2, 'drama': 3},
    'Bob': {'action': 4, 'comedy': 3, 'drama': 4},
    'Charlie': {'action': 1, 'comedy': 5, 'drama': 2},
    'David': {'action': 3, 'comedy': 2, 'drama': 5},
    'Emma': {'action': 2, 'comedy': 4, 'drama': 1}
}

# Sample movie recommendations
movies = {
    'Movie1': {'action': 2, 'comedy': 5, 'drama': 1},
    'Movie2': {'action': 3, 'comedy': 4, 'drama': 2},
    'Movie3': {'action': 5, 'comedy': 1, 'drama': 4},
    'Movie4': {'action': 1, 'comedy': 3, 'drama': 5},
    'Movie5': {'action': 4, 'comedy': 2, 'drama': 3}
}

# Function to recommend movies to a user based on their profile
def recommend_movies(user):
    recommendations = {}
    
    for movie, genres in movies.items():
        similarity = sum(user_profiles[user][genre] * genres[genre] for genre in genres)
        recommendations[movie] = similarity
    
    sorted_recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, _ in sorted_recommendations]

# Example usage
user = 'Alice'
recommended_movies = recommend_movies(user)

print(f"Recommended movies for {user}:")
for movie in recommended_movies:
    print(movie)
