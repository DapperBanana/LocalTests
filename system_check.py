
# Sample dataset of movies and their genres
movies = {
    "The Shawshank Redemption": ["Drama"],
    "The Godfather": ["Crime", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "The Lord of the Rings: The Fellowship of the Ring": ["Adventure", "Fantasy"],
    "Forrest Gump": ["Drama", "Romance"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "The Matrix": ["Action", "Sci-Fi"]
}

# Function to recommend movies based on genre
def recommend_movies(user_genre):
    recommended_movies = []
    for movie, genres in movies.items():
        for genre in genres:
            if genre in user_genre:
                recommended_movies.append(movie)
                break
    return recommended_movies

# Main program
user_genre = input("Enter your favorite movie genre: ").split(",")
recommended_movies = recommend_movies(user_genre)

if recommended_movies:
    print("Recommended movies for you:")
    for movie in recommended_movies:
        print(movie)
else:
    print("No movies found for your selected genre.")
