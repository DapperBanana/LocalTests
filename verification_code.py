
import random

def main():
    print("Welcome to the Spaceship Game!")
    print("You are the captain of a spaceship on a mission to explore the galaxy.")
    
    health = 100
    fuel = 100
    distance = 0
    
    while True:
        action = input("\nEnter your action (explore, refuel, repair, status, quit): ")
        
        if action == "explore":
            distance_traveled = random.randint(1, 10)
            fuel_used = random.randint(1, 20)
            health_loss = random.randint(1, 10)
            
            if fuel_used > fuel:
                print("Not enough fuel to explore. Refuel first.")
            else:
                distance += distance_traveled
                fuel -= fuel_used
                health -= health_loss
                
                print(f"You traveled {distance_traveled} light years, used {fuel_used} fuel, and lost {health_loss} health.")
                
        elif action == "refuel":
            fuel += random.randint(20, 50)
            print("You refueled your spaceship.")
        
        elif action == "repair":
            health += random.randint(10, 30)
            print("You repaired your spaceship.")
            
        elif action == "status":
            print(f"Distance traveled: {distance} light years")
            print(f"Fuel level: {fuel}")
            print(f"Health: {health}")
            
        elif action == "quit":
            print("Thanks for playing!")
            break
        
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
