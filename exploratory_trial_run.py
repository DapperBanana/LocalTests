
import random
import time

# Constants
ROAD_LENGTH = 20
NUM_CARS = 5

# Function to display the road with cars
def display_road(road, cars):
    for i in range(ROAD_LENGTH):
        if i in cars:
            print("X", end="")
        else:
            print("-", end="")
    print("\n")

# Function to update the car positions
def update_cars(cars):
    for i in range(NUM_CARS):
        move = random.choice([-1, 0, 1])
        cars[i] += move
        if cars[i] < 0:
            cars[i] = 0
        elif cars[i] >= ROAD_LENGTH:
            cars[i] = ROAD_LENGTH - 1

# Main simulation loop
def main():
    cars = [random.randint(0, ROAD_LENGTH-1) for _ in range(NUM_CARS)]

    while True:
        # Clear the screen
        print("\033[H\033[J")

        # Update car positions
        update_cars(cars)

        # Display the road
        display_road(ROAD_LENGTH, cars)

        # Wait for a short amount of time
        time.sleep(0.5)

if __name__ == "__main__":
    main()
