
import time

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

class Road:
    def __init__(self, length):
        self.length = length
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            if car.speed > 0:
                car.speed -= 1
            print(f"{car.name} is moving at speed {car.speed}")
    
    def add_car_at_random_speed(self, car_name):
        import random
        random_speed = random.randint(0, 10)
        self.add_car(Car(car_name, random_speed))

road = Road(10)
road.add_car_at_random_speed("Car1")
road.add_car_at_random_speed("Car2")
road.add_car_at_random_speed("Car3")

for i in range(10):
    print(f"Time step {i}")
    road.move_cars()
    road.add_car_at_random_speed(f"NewCar{i}")
    time.sleep(1)
