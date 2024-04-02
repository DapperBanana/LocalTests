
# Sample content-based recommendation system in Python

# Dummy data of movies and their genres
movies = {
    'Movie 1': ['Action', 'Adventure'],
    'Movie 2': ['Drama'],
    'Movie 3': ['Comedy', 'Romance'],
    'Movie 4': ['Action', 'Drama'],
    'Movie 5': ['Comedy']
}

# Function to get recommendations based on user input
def get_recommendations(user_input):
    recommendations = []
    
    for movie in movies:
        if set(user_input).intersection(movies[movie]):
            recommendations.append(movie)
    
    return recommendations

# Getting user input
user_input = input("Enter your preferred genres separated by comma (e.g. Action,Comedy): ")
user_input = user_input.split(',')

# Getting recommendations
recommendations = get_recommendations(user_input)

# Displaying recommendations
if recommendations:
    print("Recommended movies based on your input:\n")
    for movie in recommendations:
        print(movie)
else:
    print("No recommendations found. Please try different genres.")
