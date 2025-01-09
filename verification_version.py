
import time
import random

class Car:
    def __init__(self, speed):
        self.speed = speed

    def move(self):
        return self.speed

def main():
    road_length = 10
    cars = []
    
    for _ in range(5):
        speed = random.randint(1, 5)
        cars.append(Car(speed))
    
    while True:
        road = [' '] * road_length
        
        for car in cars:
            car_position = cars.index(car)
            road[car_position] = '>'
        
        for index, _ in enumerate(road):
            if index < len(road) - 1:
                if road[index] == '>' and road[index + 1] == ' ':
                    road[index] = ' '
                    road[index + 1] = '>'
        
        for _ in range(road_length):
            print('-', end='')
        print()
        
        for cell in road:
            print(cell, end='')
        print()
        
        for _ in range(road_length):
            print('-', end='')
        print()
        
        for car in cars:
            car.move()
        
        time.sleep(1)

if __name__ == '__main__':
    main()
