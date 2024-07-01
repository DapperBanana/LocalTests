
import numpy as np

# Create some example data with movie ratings
movies = {
    'The Shawshank Redemption': np.array([4, 5, 0, 3, 0]),
    'The Godfather': np.array([5, 4, 0, 0, 2]),
    'The Dark Knight': np.array([0, 5, 4, 0, 0]),
    'Pulp Fiction': np.array([4, 0, 0, 5, 3]),
    'Forrest Gump': np.array([0, 3, 5, 0, 4])
}

# Define a function to calculate the similarity between two movies
def calculate_similarity(movie1, movie2):
    return np.dot(movie1, movie2) / (np.linalg.norm(movie1) * np.linalg.norm(movie2))

# Define a function to recommend movies based on a given movie
def recommend_movies(movie, n=2):
    similarities = {key: calculate_similarity(movie, value) for key, value in movies.items()}
    sorted_similarities = sorted(similarities.items(), key=lambda x: x[1], reverse=True)
    recommended_movies = sorted_similarities[:n]
    return recommended_movies

# Get user input for a selected movie
selected_movie = input("Enter a movie: ")
if selected_movie in movies:
    selected_movie_vector = movies[selected_movie]
    recommended_movies = recommend_movies(selected_movie_vector)
    print("Recommended movies for", selected_movie, ":")
    for movie, similarity in recommended_movies:
        if movie != selected_movie:
            print(movie, "- Similarity:", similarity)
else:
    print("Movie not found in database.")
