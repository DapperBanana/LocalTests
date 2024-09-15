
# Movie recommendation system

# Sample movie data
movies = {
    "The Shawshank Redemption": ["Drama", "Crime"],
    "The Godfather": ["Drama", "Crime"],
    "The Dark Knight": ["Action", "Crime"],
    "Pulp Fiction": ["Drama", "Crime"],
    "Forrest Gump": ["Drama", "Romance"],
    "Inception": ["Action", "Science Fiction"],
    "The Matrix": ["Action", "Science Fiction"],
    "Interstellar": ["Science Fiction", "Drama"]
}

# Function to recommend movies based on user preferences
def recommend_movies(preferences):
    recommended_movies = set()
    for movie, genres in movies.items():
        if all(genre in preferences for genre in genres):
            recommended_movies.add(movie)
    
    if recommended_movies:
        return recommended_movies
    else:
        return None

# Main program loop
while True:
    print("Welcome to the Movie Recommendation System")
    print("Enter your movie preferences separated by commas (e.g. Action,Sci-Fi):")
    
    user_input = input()
    user_preferences = user_input.split(',')
    
    recommended_movies = recommend_movies(user_preferences)
    
    if recommended_movies:
        print("Recommended movies for you:")
        for movie in recommended_movies:
            print("-", movie)
    else:
        print("Sorry, no movies match your preferences. Please try again.")
    
    choice = input("Do you want to make another recommendation? (Y/N): ")
    if choice.lower() != 'y':
        break

print("Thank you for using the Movie Recommendation System!")
