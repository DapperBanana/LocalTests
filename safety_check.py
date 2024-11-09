
import time

class TrafficSimulation:
    def __init__(self, road_length, num_cars):
        self.road_length = road_length
        self.num_cars = num_cars
        self.road = [' '] * self.road_length

    def update_road(self):
        for i in range(self.num_cars):
            self.road[i] = 'X'
        for i in range(self.num_cars, self.road_length):
            self.road[i] = ' '

    def display_road(self):
        print(''.join(self.road))

    def run_simulation(self, num_steps):
        for _ in range(num_steps):
            self.update_road()
            self.display_road()
            time.sleep(0.5)

simulation = TrafficSimulation(20, 5)
simulation.run_simulation(10)
