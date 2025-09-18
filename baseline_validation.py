
import time
import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

def display_traffic(cars):
    for car in cars:
        print(f"{car.name}: {'-' * car.speed}")

def simulate_traffic():
    cars = [Car("Car1", random.randint(1, 5)),
            Car("Car2", random.randint(1, 5)),
            Car("Car3", random.randint(1, 5))]
    
    for _ in range(10):
        display_traffic(cars)
        time.sleep(1)
        
        for car in cars:
            car.speed = random.randint(1, 5)

simulate_traffic()
