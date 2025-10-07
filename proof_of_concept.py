
movies = {
    "The Shawshank Redemption": "Drama",
    "The Godfather": "Crime",
    "The Dark Knight": "Action",
    "Pulp Fiction": "Drama",
    "Fight Club": "Drama",
    "Goodfellas": "Crime",
    "Inception": "Sci-Fi",
    "The Matrix": "Action",
    "Jurassic Park": "Sci-Fi",
    "Titanic": "Romance"
}

print("Welcome to the movie recommendation system!")
print("Please select a genre to get a recommendation:")
for genre in set(movies.values()):
    print(genre)

selected_genre = input("Enter the genre: ")
recommendations = [movie for movie, genre in movies.items() if genre == selected_genre]

if recommendations:
    print("Here are some recommendations for you:")
    for movie in recommendations:
        print(movie)
else:
    print("Sorry, no recommendations found for that genre.")
