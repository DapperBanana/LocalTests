
# Sample movie data
movies = {
    'movie1': {'action': 3, 'comedy': 5, 'drama': 2},
    'movie2': {'action': 2, 'comedy': 4, 'drama': 3},
    'movie3': {'action': 5, 'comedy': 1, 'drama': 4},
    'movie4': {'action': 1, 'comedy': 3, 'drama': 5}
}

# Function to calculate similarity between two movies
def calculate_similarity(movie1, movie2):
    shared_categories = set(movie1.keys()) & set(movie2.keys())
    
    numerator = sum(movie1[cat] * movie2[cat] for cat in shared_categories)
    denominator = (sum(value ** 2 for value in movie1.values()) ** 0.5) * (sum(value ** 2 for value in movie2.values()) ** 0.5)
    
    if denominator == 0:
        return 0
    else:
        return numerator / denominator

# Function to recommend movies based on similarity
def recommend_movies(movie_data, movie_name, num_recommendations=2):
    similarities = {}
    
    for movie in movie_data:
        if movie != movie_name:
            similarity = calculate_similarity(movie_data[movie_name], movie_data[movie])
            similarities[movie] = similarity
    
    sorted_movies = sorted(similarities, key=similarities.get, reverse=True)[:num_recommendations]
    
    return sorted_movies

# Input movie name to get recommendations
movie_name = 'movie1'
recommendations = recommend_movies(movies, movie_name)

print(f"Recommendations for {movie_name}: {recommendations}")
