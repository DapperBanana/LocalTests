
# Define some sample data of movies and their genres
movies = {
    'Movie 1': ['Action', 'Adventure'],
    'Movie 2': ['Comedy'],
    'Movie 3': ['Drama', 'Romance'],
    'Movie 4': ['Action', 'Drama'],
    'Movie 5': ['Comedy', 'Romance']
}

# Define a function to calculate the similarity between two movies based on their genres
def calculate_similarity(movie1, movie2):
    genre_intersection = set(movies[movie1]).intersection(set(movies[movie2]))
    genre_union = set(movies[movie1]).union(set(movies[movie2]))
    similarity = len(genre_intersection) / len(genre_union)
    return similarity

# Define a function to recommend movies based on a given movie
def recommend_movies(movie):
    recommendations = []
    for other_movie in movies:
        if other_movie != movie:
            similarity = calculate_similarity(movie, other_movie)
            if similarity > 0.5:
                recommendations.append(other_movie)
    return recommendations

# Get user input for a movie
movie = input("Enter a movie: ")

# Recommend movies based on the input movie
recommended_movies = recommend_movies(movie)

# Print the recommended movies
if recommended_movies:
    print("Recommended movies based on", movie, ":")
    for recommended_movie in recommended_movies:
        print(recommended_movie)
else:
    print("No recommendations found for", movie)
