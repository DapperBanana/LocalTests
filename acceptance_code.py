
import random
import time

class Car:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def move(self):
        self.position += random.randint(1, 5)

class TrafficSimulation:
    def __init__(self, num_cars):
        self.cars = [Car(f"Car {i+1}") for i in range(num_cars)]

    def display_state(self):
        for car in self.cars:
            print(f"{car.name}: {'-' * car.position}>")

    def run_simulation(self, num_iterations):
        for _ in range(num_iterations):
            for car in self.cars:
                car.move()
            self.display_state()
            time.sleep(1)

sim = TrafficSimulation(5)
sim.run_simulation(10)
