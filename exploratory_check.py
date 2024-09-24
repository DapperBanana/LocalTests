
import time
import random

class Vehicle:
    def __init__(self, name):
        self.name = name
        self.speed = random.randint(40, 80)
    
    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h")
    
class TrafficSimulation:
    def __init__(self, num_vehicles):
        self.vehicles = [Vehicle(f"Vehicle {i+1}") for i in range(num_vehicles)]
    
    def run(self, duration):
        for i in range(duration):
            print(f"Time: {i+1}")
            for vehicle in self.vehicles:
                vehicle.move()
            time.sleep(1)

# Create a traffic simulation with 5 vehicles
sim = TrafficSimulation(5)

# Run the simulation for 10 seconds
sim.run(10)
