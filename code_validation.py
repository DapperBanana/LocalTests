
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

    def update_simulation(self):
        for car in self.cars:
            car.move()

    def display_simulation(self):
        road = [" "]*self.road_length
        for car in self.cars:
            if car.position < self.road_length:
                road[car.position] = car.name
        print("".join(road))

def main():
    car1 = Car("A", 1, 0)
    car2 = Car("B", 2, 0)
    car3 = Car("C", 3, 0)

    simulation = TrafficSimulation(20, [car1, car2, car3])

    for i in range(10):
        simulation.update_simulation()
        simulation.display_simulation()
        time.sleep(1)

if __name__ == "__main__":
    main()
