
import random
import time

class TrafficSimulation:
    def __init__(self, road_length, car_density, max_speed):
        self.road_length = road_length
        self.car_density = car_density
        self.max_speed = max_speed
        self.road = ['_' for _ in range(road_length)]
        self.cars = []

        for i in range(road_length):
            if random.random() < car_density:
                speed = random.randint(1, max_speed)
                self.cars.append((i, speed))

    def update(self):
        new_cars = []
        for i, speed in self.cars:
            new_speed = min(speed + 1, self.max_speed)
            new_cars.append((i + new_speed, new_speed))

        self.road = ['_' for _ in range(self.road_length)]
        for i, speed in new_cars:
            if i < self.road_length:
                self.road[i] = '#'

        self.cars = [(i, speed) for i, speed in new_cars if i < self.road_length]

    def display(self):
        print(''.join(self.road))

road_length = 50
car_density = 0.3
max_speed = 5
sim = TrafficSimulation(road_length, car_density, max_speed)

while True:
    sim.update()
    sim.display()
    time.sleep(0.5)
