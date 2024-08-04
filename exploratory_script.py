
# Define a dictionary of movies and their corresponding genres
movies = {
    "The Matrix": "Action",
    "The Shawshank Redemption": "Drama",
    "Forrest Gump": "Drama",
    "The Dark Knight": "Action",
    "Pulp Fiction": "Crime",
    "Inception": "Sci-Fi",
    "The Godfather": "Crime"
}

# Function to recommend movies based on user input
def recommend_movie(genre):
    recommended_movies = []
    for movie, movie_genre in movies.items():
        if genre.lower() == movie_genre.lower():
            recommended_movies.append(movie)
    if len(recommended_movies) == 0:
        return "Sorry, we don't have any recommendations for that genre."
    else:
        return recommended_movies

# Main program loop
while True:
    print("Welcome to the movie recommendation system!")
    print("Enter a movie genre or 'quit' to exit.")
    
    user_input = input("Enter a movie genre: ")
    
    if user_input.lower() == 'quit':
        print("Thank you for using the movie recommendation system. Goodbye!")
        break
    
    recommended_movies = recommend_movie(user_input)
    for movie in recommended_movies:
        print(movie)
