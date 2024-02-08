
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Sample data of user preferences
user_preferences = {
    'user_1': {
        'action': 5,
        'adventure': 2,
        'comedy': 0,
        'drama': 4,
        'horror': 1
    },
    'user_2': {
        'action': 1,
        'adventure': 5,
        'comedy': 2,
        'drama': 3,
        'horror': 4
    },
    'user_3': {
        'action': 2,
        'adventure': 3,
        'comedy': 4,
        'drama': 1,
        'horror': 5
    }
}

# List of movies
movies = ['movie_1', 'movie_2', 'movie_3', 'movie_4', 'movie_5']

# Features of movies
movie_features = np.array([
    [5, 3, 0, 2, 1],  # movie_1
    [1, 4, 0, 5, 4],  # movie_2
    [2, 2, 0, 4, 5],  # movie_3
    [4, 4, 0, 1, 2],  # movie_4
    [3, 5, 0, 3, 0]   # movie_5
])

# Function to calculate similarity score using cosine similarity
def calculate_similarity(user_preferences, movie_features):
    similarity_scores = {}

    for user, preferences in user_preferences.items():
        user_vector = np.array(list(preferences.values())).reshape(1, -1)
        similarity_scores[user] = cosine_similarity(user_vector, movie_features).flatten().tolist()

    return similarity_scores

# Get similarity scores
similarity_scores = calculate_similarity(user_preferences, movie_features)

# Function to get top recommended movies for a user
def get_recommendations(user, n_recommendations=3):
    if user not in similarity_scores:
        return []

    user_similarity = similarity_scores[user]
    top_indices = np.argsort(user_similarity)[-n_recommendations:][::-1]

    return [movies[i] for i in top_indices]

# Get recommendations for a user
user = 'user_1'
recommendations = get_recommendations(user)

# Print recommendations
if recommendations:
    print(f"Top 3 movie recommendations for {user}:")
    for i, movie in enumerate(recommendations):
        print(f"{i+1}. {movie}")
else:
    print(f"No recommendations found for {user}")
