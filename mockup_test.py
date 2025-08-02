
class FitnessTracker:
    def __init__(self):
        self.steps = 0
        self.calories_burned = 0
        self.workouts_completed = 0
    
    def record_steps(self, steps):
        self.steps += steps
    
    def record_calories_burned(self, calories):
        self.calories_burned += calories
    
    def record_workout_completed(self):
        self.workouts_completed += 1
    
    def display_stats(self):
        print("Fitness Tracker Stats:")
        print(f"Steps: {self.steps}")
        print(f"Calories Burned: {self.calories_burned}")
        print(f"Workouts Completed: {self.workouts_completed}")

# Main program
tracker = FitnessTracker()

while True:
    print("\n1. Record Steps")
    print("2. Record Calories Burned")
    print("3. Record Workout Completed")
    print("4. Display Stats")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        steps = int(input("Enter number of steps: "))
        tracker.record_steps(steps)
    elif choice == '2':
        calories = int(input("Enter calories burned: "))
        tracker.record_calories_burned(calories)
    elif choice == '3':
        tracker.record_workout_completed()
    elif choice == '4':
        tracker.display_stats()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
