
# Define a dictionary of movie genres and corresponding movie titles
movies = {
    'action': ['The Avengers', 'Die Hard', 'Mad Max: Fury Road'],
    'comedy': ['Superbad', 'Anchorman', 'Bridesmaids'],
    'drama': ['The Shawshank Redemption', 'The Godfather', 'Forrest Gump']
}

# Function to recommend movies based on user input
def recommend_movie(genre):
    if genre.lower() in movies:
        recommended_movies = movies[genre.lower()]
        return recommended_movies
    else:
        return "Sorry, we don't have any recommendations for that genre."

# Main program loop
while True:
    user_input = input("Enter a movie genre to get recommendations (action, comedy, drama): ")

    recommended_movies = recommend_movie(user_input)

    print("Recommended Movies:")
    for movie in recommended_movies:
        print(movie)

    continue_input = input("Do you want to get more movie recommendations? (yes/no) ")
    if continue_input.lower() != 'yes':
        break
