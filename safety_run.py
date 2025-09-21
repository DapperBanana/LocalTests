
import time
import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class TrafficSimulation:
    def __init__(self):
        self.cars = []
        self.lane_length = 20
        self.traffic = ['-'] * self.lane_length

    def add_car(self, name, speed):
        car = Car(name, speed)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            distance = car.speed
            if car in self.cars[:-1]:
                index = self.traffic.index(car.name)
                next_car = self.cars[self.cars.index(car) + 1]
                next_car_index = self.traffic.index(next_car.name)
                distance = next_car_index - index - 1
            if index + distance >= self.lane_length:
                self.traffic[index] = '-'
                continue
            self.traffic[index] = '-'
            self.traffic[index + distance] = car.name

    def display_traffic(self):
        print(''.join(self.traffic))

    def run_simulation(self, num_steps):
        for step in range(num_steps):
            print(f"Step {step+1}:")
            self.move_cars()
            self.display_traffic()
            time.sleep(1)

sim = TrafficSimulation()
sim.add_car('A', 2)
sim.add_car('B', 1)

sim.run_simulation(10)
