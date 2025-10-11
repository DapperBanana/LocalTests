
import numpy as np

# Sample data of movie ratings for each genre
user_ratings = {
    'action': 5,
    'comedy': 2,
    'drama': 4,
    'horror': 1,
    'romance': 3
}

# Sample data of movie profiles by genre
movie_profiles = {
    'movie1': {'action': 4, 'comedy': 2, 'drama': 3, 'horror': 1, 'romance': 2},
    'movie2': {'action': 2, 'comedy': 4, 'drama': 1, 'horror': 3, 'romance': 2},
    'movie3': {'action': 4, 'comedy': 1, 'drama': 2, 'horror': 3, 'romance': 3},
    'movie4': {'action': 1, 'comedy': 3, 'drama': 2, 'horror': 4, 'romance': 1},
    'movie5': {'action': 3, 'comedy': 2, 'drama': 4, 'horror': 1, 'romance': 3},
}

# Calculate similarity between user ratings and movie profiles
def calculate_similarity(user_ratings, movie_profiles):
    similarities = {}
    for movie, profile in movie_profiles.items():
        rating = np.array(list(user_ratings.values()))
        profile = np.array(list(profile.values()))
        similarity = np.dot(rating, profile) / (np.linalg.norm(rating) * np.linalg.norm(profile))
        similarities[movie] = similarity
    return similarities

# Recommend top n movies based on similarity
def recommend_movies(user_ratings, movie_profiles, n=3):
    similarities = calculate_similarity(user_ratings, movie_profiles)
    recommended_movies = sorted(similarities, key=similarities.get, reverse=True)[:n]
    return recommended_movies

# Get recommendations for the user
print("Recommended movies:", recommend_movies(user_ratings, movie_profiles, 3))
