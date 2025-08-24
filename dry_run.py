
import time

class TrafficSimulation:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def run_simulation(self, duration):
        for _ in range(duration):
            for car in self.cars:
                car.move()
            self.display()
            time.sleep(1)
    
    def display(self):
        road = ['_' for _ in range(10)]
        for car in self.cars:
            road[car.position] = car.symbol
        print(''.join(road))

class Car:
    def __init__(self, symbol, position):
        self.symbol = symbol
        self.position = position
    
    def move(self):
        self.position += 1
        if self.position >= 10:
            self.position = 0

sim = TrafficSimulation()
sim.add_car(Car('A', 0))
sim.add_car(Car('B', 4))

sim.run_simulation(10)
