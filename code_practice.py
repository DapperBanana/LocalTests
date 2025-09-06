
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories = 0
    
    def log_steps(self, steps):
        self.steps += steps
    
    def log_calories(self, calories):
        self.calories += calories
    
    def display_stats(self):
        print("Fitness Tracker Stats:")
        print("Steps taken:", self.steps)
        print("Calories burned:", self.calories)

def main():
    tracker = FitnessTracker()
    
    while True:
        print("\n1. Log Steps")
        print("2. Log Calories")
        print("3. Display Stats")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            steps = int(input("Enter the number of steps taken: "))
            tracker.log_steps(steps)
        elif choice == '2':
            calories = int(input("Enter the number of calories burned: "))
            tracker.log_calories(calories)
        elif choice == '3':
            tracker.display_stats()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
