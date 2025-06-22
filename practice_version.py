
import random

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
player_location = random.choice(planets)

print('Welcome to the Space Exploration Game!')
print('You are currently on planet', player_location)

while True:
    action = input('What would you like to do? (explore/travel/quit): ')
    
    if action == 'explore':
        print('You look around and see a vast expanse of stars and planets.')
    elif action == 'travel':
        new_location = random.choice(planets)
        while new_location == player_location:
            new_location = random.choice(planets)
        player_location = new_location
        print('You traveled to planet', player_location)
    elif action == 'quit':
        print('Thanks for playing! Goodbye.')
        break
    else:
        print('Invalid input. Please try again.')
