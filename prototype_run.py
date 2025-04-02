
# List of movie genres
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi']

# Dictionary of movies with their corresponding genres
movies = {
    'Die Hard': 'Action',
    'The Hangover': 'Comedy',
    'The Shawshank Redemption': 'Drama',
    'The Exorcist': 'Horror',
    'Blade Runner': 'Sci-Fi'
}

def recommend_movie(genre):
    recommended_movies = [movie for movie, movie_genre in movies.items() if movie_genre == genre]
    
    if recommended_movies:
        print(f"Recommended movies in the {genre} genre:")
        for movie in recommended_movies:
            print(movie)
    else:
        print(f"No movies found in the {genre} genre.")

# Main program
print("Welcome to the Movie Recommendation System!")

while True:
    print("\nSelect a genre to get movie recommendations:")
    for index, genre in enumerate(genres, 1):
        print(f"{index}. {genre}")
    
    choice = input("Enter the number corresponding to the genre (1-5) or 'q' to quit: ")
    
    if choice == 'q':
        print("Thank you for using the Movie Recommendation System. Goodbye!")
        break
    elif choice.isdigit():
        genre_index = int(choice) - 1
        
        if genre_index in range(len(genres)):
            recommend_movie(genres[genre_index])
        else:
            print("Invalid choice. Please try again.")
    else:
        print("Invalid input. Please try again.")
