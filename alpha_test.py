
# Sample dataset of movies and their genres
dataset = {
    'The Godfather': ['Crime', 'Drama'],
    'Inception': ['Action', 'Adventure', 'Sci-Fi'],
    'The Shawshank Redemption': ['Drama'],
    'Pulp Fiction': ['Crime', 'Drama'],
    'The Dark Knight': ['Action', 'Crime', 'Drama']
}

# Function to calculate similarity score between two movies based on genres
def calculate_similarity(movie1, movie2):
    genre_set1 = set(dataset[movie1])
    genre_set2 = set(dataset[movie2])
    
    common_genres = genre_set1.intersection(genre_set2)
    
    similarity_score = len(common_genres) / (len(genre_set1) + len(genre_set2))
    
    return similarity_score

# Function to recommend movies based on a target movie
def recommend_movies(target_movie):
    similarity_scores = {}
    
    for movie in dataset:
        if movie != target_movie:
            score = calculate_similarity(target_movie, movie)
            similarity_scores[movie] = score
    
    sorted_scores = sorted(similarity_scores.items(), key=lambda x: x[1], reverse=True)
    
    recommended_movies = []
    for movie, score in sorted_scores:
        recommended_movies.append(movie)
    
    return recommended_movies

# Main program
target_movie = 'The Godfather'
recommended_movies = recommend_movies(target_movie)

print(f"Recommended movies for {target_movie}:")
for movie in recommended_movies:
    print(movie)
