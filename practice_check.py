
# List of movies and their respective genres
movies = {
    "The Godfather": "Crime",
    "Inception": "Sci-Fi",
    "The Shawshank Redemption": "Drama",
    "The Dark Knight": "Action",
    "Pulp Fiction": "Crime",
}

# Function to recommend movies based on genre
def recommend_movie(genre):
    recommended_movies = [movie for movie, movie_genre in movies.items() if movie_genre == genre]
    return recommended_movies

# Main program loop
while True:
    print("Welcome to the Movie Recommendation System!")
    print("Available genres: ")
    for genre in set(movies.values()):
        print(genre)

    user_genre = input("Enter a genre to get movie recommendations (or enter 'exit' to quit): ")

    if user_genre == 'exit':
        break
    elif user_genre in set(movies.values()):
        recommended_movies = recommend_movie(user_genre)
        print("Recommended movies in the", user_genre, "genre:")
        for movie in recommended_movies:
            print("-", movie)
    else:
        print("Invalid genre. Please try again.")
