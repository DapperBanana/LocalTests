
import time

def traffic_simulation(num_cars, road_length, simulation_time):
    road = ['_' for _ in range(road_length)]
    
    cars = [{'position': 0, 'speed': 1} for _ in range(num_cars)]
    
    for _ in range(simulation_time):
        for car in cars:
            if car['position'] < road_length-1:
                road[car['position']] = '_'
                car['position'] += car['speed']
                road[car['position']] = 'X'
        
        print(''.join(road))
        time.sleep(0.5)
    
    print("Simulation over")
    
# Set the parameters for the simulation
num_cars = 5
road_length = 20
simulation_time = 10

# Run the simulation
traffic_simulation(num_cars, road_length, simulation_time)
