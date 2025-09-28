
import time
import random

class TrafficSimulator:
    def __init__(self, num_cars, road_length):
        self.num_cars = num_cars
        self.road_length = road_length
        self.cars = []
        for i in range(num_cars):
            self.cars.append(random.randint(0, road_length))
    
    def run(self, num_steps):
        for step in range(num_steps):
            road = [' '] * self.road_length
            for car_pos in self.cars:
                road[car_pos] = '*'
            
            print(''.join(road))
            
            for i in range(len(self.cars)):
                self.cars[i] += random.choice([-1, 1])
                self.cars[i] = max(0, self.cars[i])
                self.cars[i] = min(self.road_length - 1, self.cars[i])
            
            time.sleep(0.5)

if __name__ == '__main__':
    num_cars = 5
    road_length = 20
    sim = TrafficSimulator(num_cars, road_length)
    sim.run(20)
