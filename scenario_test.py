
# Define some sample data for content-based recommendation
movies = {
    'movie1': {
        'genre': 'Action',
        'year': 2000
    },
    'movie2': {
        'genre': 'Comedy',
        'year': 2005
    },
    'movie3': {
        'genre': 'Drama',
        'year': 2010
    },
    'movie4': {
        'genre': 'Action',
        'year': 2015
    },
    'movie5': {
        'genre': 'Comedy',
        'year': 2020
    }
}

# Function to recommend movies based on genre and year
def recommend_movies(user_preferences):
    recommended_movies = []
    for movie, info in movies.items():
        if info['genre'] in user_preferences['genre'] and info['year'] >= user_preferences['year']:
            recommended_movies.append(movie)
    
    return recommended_movies

# Define user preferences
user_preferences = {
    'genre': ['Action'],
    'year': 2010
}

# Get recommended movies
recommended_movies = recommend_movies(user_preferences)

# Print recommended movies
print("Recommended movies:")
for movie in recommended_movies:
    print(movie)
