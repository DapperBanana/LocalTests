
import time

# Define the road with 10 spaces
road = [' '] * 10

# Define the initial position of the car
car_position = 0

# Define the car symbol
car_symbol = 'C'

# Define the simulation speed
simulation_speed = 0.5

# Function to display the road
def display_road():
    print(''.join(road))

# Main simulation loop
while True:
    # Clear the road
    road[car_position] = ' '
    
    # Move the car
    car_position += 1
    
    # Check if the car reached the end of the road
    if car_position >= len(road):
        break
    
    # Update the road with the car symbol
    road[car_position] = car_symbol
    
    # Display the road
    display_road()
    
    # Wait for a few seconds
    time.sleep(simulation_speed)
