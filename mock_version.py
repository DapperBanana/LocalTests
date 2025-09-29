
# Movie recommendation system

# Dictionary of movie genres and corresponding movies
movies = {
    'Action': ['The Dark Knight', 'Avengers: Infinity War', 'Mad Max: Fury Road'],
    'Comedy': ['Superbad', 'Anchorman', 'Bridesmaids'],
    'Drama': ['The Shawshank Redemption', 'Forrest Gump', 'The Godfather'],
    'Sci-Fi': ['Blade Runner 2049', 'Inception', 'Interstellar']
}

# Function to recommend movies based on genre
def recommend_movie():
    genre = input("Enter your preferred movie genre (Action, Comedy, Drama, Sci-Fi): ")
    
    if genre in movies:
        recommended_movies = movies[genre]
        print("\nRecommended movies in the", genre, "genre:")
        for movie in recommended_movies:
            print("- " + movie)
    else:
        print("Sorry, we don't have any recommendations for that genre.")

# Main program loop
while True:
    print("\nWelcome to the Movie Recommendation System!")
    print("Select an option:")
    print("1. Get movie recommendations")
    print("2. Exit")
    
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        recommend_movie()
    elif choice == '2':
        print("Thank you for using the Movie Recommendation System. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter either 1 or 2.")
