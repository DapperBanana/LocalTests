
import time

def show_traffic(light):
    print("Traffic Light Status:")
    
    if light == "red":
        print("   Red light : [X]")
        print("   Green light : [ ]")
    else:
        print("   Red light : [ ]")
        print("   Green light : [X]")

def simulate_traffic():
    light = "red"
    
    while True:
        show_traffic(light)
        time.sleep(2)
        
        light = "green" if light == "red" else "red"

def main():
    print("Welcome to the Traffic Simulation!")
    
    while True:
        choice = input("Press 's' to start the simulation or 'q' to quit: ")
        
        if choice == "s":
            simulate_traffic()
        elif choice == "q":
            break
        else:
            print("Invalid choice! Try again.")
    
    print("Thanks for using the Traffic Simulation!")

if __name__ == "__main__":
    main()
