
# Define a dictionary of movies and their genres
movies = {
    "The Dark Knight": "Action",
    "Inception": "Sci-Fi",
    "The Shawshank Redemption": "Drama",
    "Pulp Fiction": "Crime",
    "The Godfather": "Crime"
}

# Function to recommend a movie based on user input
def recommend_movie(genre):
    recommended_movies = []
    for movie, movie_genre in movies.items():
        if movie_genre == genre:
            recommended_movies.append(movie)
    if recommended_movies:
        return recommended_movies
    else:
        return "No movies found in that genre."

# Main program loop
while True:
    # Get user input for genre
    user_input = input("Enter a movie genre (Action, Sci-Fi, Drama, Crime): ")
    recommended_list = recommend_movie(user_input)
    
    # Print recommended movies
    if isinstance(recommended_list, list):
        print("Recommended movies in the", user_input, "genre:")
        for movie in recommended_list:
            print("-", movie)
    else:
        print(recommended_list)
        
    # Ask user if they want to continue
    continue_input = input("Do you want to get recommendations for another genre? (y/n): ")
    if continue_input.lower() != "y":
        break
