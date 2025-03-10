
# Movie recommendation system

# Define a list of movies and their corresponding genres
movies = [
    {"title": "The Godfather", "genre": "Drama"},
    {"title": "The Shawshank Redemption", "genre": "Drama"},
    {"title": "Inception", "genre": "Sci-Fi"},
    {"title": "The Dark Knight", "genre": "Action"},
    {"title": "Pulp Fiction", "genre": "Crime"}
]

# Function to recommend movies based on genre
def recommend_movie(genre):
    recommended_movies = [movie["title"] for movie in movies if movie["genre"] == genre]
    return recommended_movies

# Main program loop
while True:
    print("\nWelcome to the Movie Recommendation System!")
    print("Choose a genre to get movie recommendations:")
    print("1. Drama")
    print("2. Sci-Fi")
    print("3. Action")
    print("4. Crime")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        recommended_movies = recommend_movie("Drama")
        print("Recommended Drama movies:")
        for movie in recommended_movies:
            print(movie)
    elif choice == "2":
        recommended_movies = recommend_movie("Sci-Fi")
        print("Recommended Sci-Fi movies:")
        for movie in recommended_movies:
            print(movie)
    elif choice == "3":
        recommended_movies = recommend_movie("Action")
        print("Recommended Action movies:")
        for movie in recommended_movies:
            print(movie)
    elif choice == "4":
        recommended_movies = recommend_movie("Crime")
        print("Recommended Crime movies:")
        for movie in recommended_movies:
            print(movie)
    elif choice == "5":
        print("Thank you for using the Movie Recommendation System!")
        break
    else:
        print("Invalid choice. Please try again.")
