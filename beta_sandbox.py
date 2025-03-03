
# Define a list of movies and their genres
movies = {
    'The Shawshank Redemption': 'Drama',
    'The Godfather': 'Crime',
    'The Dark Knight': 'Action',
    'Forrest Gump': 'Drama',
    'Inception': 'Sci-Fi',
    'Pulp Fiction': 'Crime',
    'Goodfellas': 'Crime',
    'The Matrix': 'Action',
    'Interstellar': 'Sci-Fi',
    'Fight Club': 'Drama'
}

# Get user input for their favorite genre
user_input = input("Enter your favorite movie genre: ")

# Create a list of recommended movies based on user input
recommended_movies = [movie for movie, genre in movies.items() if genre == user_input]

# Print out the recommended movies
if recommended_movies:
    print("Recommended movies in the {} genre:".format(user_input))
    for movie in recommended_movies:
        print("- {}".format(movie))
else:
    print("Sorry, no movies found in the {} genre.".format(user_input))
