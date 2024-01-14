
import random

# List of movies
movies = [
    'The Shawshank Redemption',
    'The Godfather',
    'Pulp Fiction',
    'Fight Club',
    'Forrest Gump',
    'The Dark Knight',
    'Goodfellas',
    'The Matrix',
    'Inception',
    'The Silence of the Lambs'
]

print('Welcome to the Movie Recommendation System!')
print('Here are 5 random movie recommendations for you:')

# Generate 5 random recommendations
recommendations = random.sample(movies, 5)

for i, movie in enumerate(recommendations):
    print(f'{i+1}. {movie}')

# Ask for user input
choice = int(input('Enter the number of the movie you would like to learn more about: '))

# Validate user input
while choice < 1 or choice > 5:
    print('Invalid choice. Please try again.')
    choice = int(input('Enter the number of the movie you would like to learn more about: '))

# Display the selected movie
selected_movie = recommendations[choice-1]
print(f'You have selected "{selected_movie}".')

# Ask for user rating
rating = int(input('Please rate the movie on a scale of 1 to 5: '))

# Generate a random recommendation based on rating
if rating == 1:
    print('We are sorry you did not enjoy the movie. Here is another recommendation for you:')
    new_recommendation = random.choice(movies)
    print(new_recommendation)
else:
    print('Thank you for your rating.')
