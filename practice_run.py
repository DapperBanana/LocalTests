
import random

print("Welcome to the Spaceship Game!")
print("Your mission is to reach the end of the galaxy without running out of fuel.")

fuel = 100
distance = 0

while fuel > 0 and distance < 100:
    print("\nDistance traveled: ", distance, " light years")
    print("Fuel remaining: ", fuel, "%")

    choice = input("Choose your action: [f]ly or [r]efuel\n")

    if choice == 'f':
        fuel_usage = random.randint(5, 20)
        distance_traveled = random.randint(10, 30)
        
        fuel -= fuel_usage
        distance += distance_traveled
        
        print("You traveled ", distance_traveled, " light years")
        if fuel <= 0:
            print("You ran out of fuel and lost the game.")
    elif choice == 'r':
        fuel += random.randint(20, 50)
        print("You refueled your spaceship.")
    else:
        print("Invalid choice. Try again.")

if distance >= 100:
    print("Congratulations! You have reached the end of the galaxy!")
