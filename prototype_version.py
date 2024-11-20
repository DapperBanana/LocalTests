
import time

class Car:
    def __init__(self):
        self.position = 0
        self.speed = 1

    def move(self):
        self.position += self.speed

class Road:
    def __init__(self, length):
        self.length = length
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def update(self):
        for car in self.cars:
            car.move()

    def display(self):
        road = ['-' for _ in range(self.length)]
        for car in self.cars:
            if car.position < self.length:
                road[car.position] = '*'
        print(''.join(road))


road_length = 20
road = Road(road_length)

car1 = Car()
car2 = Car()
car3 = Car()

road.add_car(car1)
road.add_car(car2)
road.add_car(car3)

while True:
    road.display()
    road.update()
    time.sleep(1)
