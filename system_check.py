
import time

class TrafficSimulation:
    def __init__(self):
        self.road = ['_' for _ in range(10)]  # create a road with 10 empty spaces
        self.car_position = 0  # start with the car at position 0

    def move_car(self):
        self.road[self.car_position] = '_'  # clear current position
        self.car_position = (self.car_position + 1) % 10  # move car to the next position
        self.road[self.car_position] = 'X'  # mark new position with car

    def display_road(self):
        print(' '.join(self.road))  # print the road status

    def run_simulation(self, duration):
        start_time = time.time()
        while time.time() - start_time < duration:
            self.move_car()
            self.display_road()
            time.sleep(0.5)

# Create an instance of TrafficSimulation and run the simulation for 10 seconds
simulation = TrafficSimulation()
simulation.run_simulation(10)
