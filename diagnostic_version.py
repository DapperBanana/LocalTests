
# Define sample content for recommendation
movies = {
    "movie1": {
        "genre": "Action",
        "director": "Director A",
        "year": 2000
    },
    "movie2": {
        "genre": "Comedy",
        "director": "Director B",
        "year": 2010
    },
    "movie3": {
        "genre": "Drama",
        "director": "Director C",
        "year": 2015
    }
}

# Function to recommend movies based on user input
def get_recommendations(user_input):
    recommendations = []
    
    for movie in movies:
        if (user_input["genre"] == movies[movie]["genre"] and
            user_input["director"] == movies[movie]["director"] and
            abs(user_input["year"] - movies[movie]["year"]) <= 5):
            recommendations.append(movie)
    
    return recommendations

# Get user input for genre, director, and year
user_input = {
    "genre": input("Enter your preferred genre: "),
    "director": input("Enter your preferred director: "),
    "year": int(input("Enter your preferred release year: "))
}

# Get movie recommendations based on user input
recommended_movies = get_recommendations(user_input)

# Display recommendations
if recommended_movies:
    print("Recommended movies:")
    for movie in recommended_movies:
        print("- " + movie)
else:
    print("No recommendations found based on your preferences.")
