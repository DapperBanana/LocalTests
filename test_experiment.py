
# Define a dictionary of movie genres and corresponding movies
movie_genres = {
    "Action": ["The Avengers", "Die Hard", "Mad Max: Fury Road"],
    "Comedy": ["Superbad", "Bridesmaids", "Anchorman"],
    "Drama": ["The Shawshank Redemption", "Titanic", "Forrest Gump"],
    "Horror": ["The Shining", "Get Out", "A Quiet Place"]
}

# Ask the user for their preferred movie genre
print("Welcome to the Movie Recommendation System!")
print("Here are the available genres:")
for genre in movie_genres.keys():
    print("- " + genre)

user_genre = input("Enter your preferred movie genre: ")

# Check if the user-selected genre is in the dictionary
if user_genre in movie_genres:
    recommended_movies = movie_genres[user_genre]
    print("Here are some recommended movies in the " + user_genre + " genre:")
    for movie in recommended_movies:
        print("- " + movie)
else:
    print("Sorry, the genre you entered is not valid. Please try again.")
