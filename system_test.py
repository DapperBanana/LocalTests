
import time

def simulate_traffic(num_cars, num_iterations):
    road = [' '] * 20  # represents a 20-unit long road
    cars = ['>' for _ in range(num_cars)]  # represent cars on the road

    for _ in range(num_iterations):
        for i in range(len(cars)):
            if cars[i] == '>':
                road[i] = ' '
                if i + 1 < len(road):
                    road[i + 1] = '>'
                    cars[i] = ' '
                    cars[i + 1] = '>'

        print(''.join(road))
        time.sleep(0.5)

    print('Simulation done!')

if __name__ == '__main__':
    num_cars = 5
    num_iterations = 10
    simulate_traffic(num_cars, num_iterations)
