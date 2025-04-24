
class FitnessTracker:
    def __init__(self, name):
        self.name = name
        self.steps = 0
        self.calories = 0

    def track_steps(self, steps):
        self.steps += steps

    def track_calories(self, calories):
        self.calories += calories

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Total Steps: {self.steps}")
        print(f"Total Calories Burned: {self.calories}")

# Main function to run the program
def main():
    tracker = FitnessTracker("John")
    
    while True:
        print("Fitness Tracking System")
        print("1. Track Steps")
        print("2. Track Calories")
        print("3. Display Stats")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            steps = int(input("Enter the number of steps: "))
            tracker.track_steps(steps)
        elif choice == "2":
            calories = int(input("Enter the number of calories burned: "))
            tracker.track_calories(calories)
        elif choice == "3":
            tracker.display_stats()
        elif choice == "4":
            print("Quitting program.")
            break
        else:
            print("Invalid choice. Please try again.")
            

if __name__ == "__main__":
    main()
