
movies = {
    "The Shawshank Redemption": ["Drama"],
    "The Godfather": ["Crime", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
    "Forrest Gump": ["Drama", "Romance"],
    "Inception": ["Action", "Adventure", "Sci-Fi"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Interstellar": ["Adventure", "Drama", "Sci-Fi"],
    "Fight Club": ["Drama"],
    "Goodfellas": ["Crime", "Drama"]
}

def recommend_movie(genre):
    recommended_movies = [movie for movie, genres in movies.items() if genre in genres]
    if recommended_movies:
        return recommended_movies
    else:
        return ["Sorry, no movies in that genre found."]

while True:
    genre = input("Enter a genre (or 'q' to quit): ")
    if genre == "q":
        break

    recommended_movies = recommend_movie(genre)
    for movie in recommended_movies:
        print(movie)
