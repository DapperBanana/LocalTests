
import time

class Car:
    def __init__(self, name, speed, position):
        self.name = name
        self.speed = speed
        self.position = position
    
    def move(self):
        self.position += self.speed

class TrafficSimulation:
    def __init__(self, road_length, cars):
        self.road_length = road_length
        self.cars = cars
    
    def display_road(self):
        road = ['-'] * self.road_length
        for car in self.cars:
            if car.position < self.road_length:
                road[car.position] = car.name
        print(''.join(road))
    
    def simulate(self):
        while True:
            self.display_road()
            time.sleep(0.5)
            
            for car in self.cars:
                car.move()
                if car.position >= self.road_length:
                    print(f'{car.name} has reached the destination!')
                    self.cars.remove(car)
            
            if not self.cars:
                print('All cars have reached their destinations!')
                break


if __name__ == '__main__':
    car1 = Car('A', 1, 0)
    car2 = Car('B', 2, 0)
    car3 = Car('C', 3, 0)
    
    simulation = TrafficSimulation(10, [car1, car2, car3])
    simulation.simulate()
