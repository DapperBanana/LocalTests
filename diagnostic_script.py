
# list of movies and their genres
movies = {
    'The Shawshank Redemption': 'Drama',
    'The Godfather': 'Crime',
    'The Dark Knight': 'Action',
    'Pulp Fiction': 'Crime',
    'Forrest Gump': 'Drama',
    'The Matrix': 'Action',
    'Schindler\'s List': 'Drama',
    'Goodfellas': 'Crime',
}

# function to recommend a movie based on user input
def recommend_movie(genre):
    recommended_movies = []
    for title, movie_genre in movies.items():
        if movie_genre == genre:
            recommended_movies.append(title)
    if recommended_movies:
        print(f"Recommended movies in the {genre} genre:")
        for movie in recommended_movies:
            print(movie)
    else:
        print(f"No movies found in the {genre} genre.")

# main program loop
while True:
    print("Welcome to the Movie Recommendation System")
    print("Select a movie genre to get recommendations (type 'exit' to quit)")
    genre = input("Enter a genre: ")
    
    if genre.lower() == 'exit':
        break
    
    recommend_movie(genre)

print("Thank you for using the Movie Recommendation System!")
