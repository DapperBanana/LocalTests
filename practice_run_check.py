
import time

def simulate_traffic(num_cars, road_length):
    road = [' '] * road_length
    cars = [(i, 0) for i in range(num_cars)]

    while True:
        for car in cars:
            road[car[1]] = 'C'

        print(''.join(road))

        time.sleep(0.5)

        for car_index, car_position in enumerate(cars):
            road[car_position[1]] = ' '
            new_position = car_position[1] + 1
            if new_position < road_length:
                cars[car_index] = (car_position[0], new_position)
        
        if cars[-1][1] == road_length:
            break

if __name__ == '__main__':
    num_cars = 5
    road_length = 10

    simulate_traffic(num_cars, road_length)
