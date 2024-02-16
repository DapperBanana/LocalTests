
import time

class Car:
    def __init__(self, name, speed, position):
        self.name = name
        self.speed = speed
        self.position = position

    def move(self):
        self.position += self.speed

    def get_position(self):
        return self.position

    def get_name(self):
        return self.name


def print_traffic(cars):
    for car in cars:
        print(car.get_name() + ": " + "-" * car.get_position())


def simulate_traffic():
    cars = []
    num_cars = int(input("Enter the number of cars: "))

    for i in range(num_cars):
        name = input("Enter car name: ")
        speed = int(input("Enter car speed: "))
        cars.append(Car(name, speed, 0))
    
    duration = int(input("Enter simulation duration (in seconds): "))
    interval = int(input("Enter simulation interval (in seconds): "))
    iterations = duration // interval
    
    for i in range(iterations):
        print("\nSimulation time: " + str(i*interval) + " seconds")
        print_traffic(cars)
        time.sleep(interval)
        for car in cars:
            car.move()


simulate_traffic()
